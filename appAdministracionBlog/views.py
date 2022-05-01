from django.shortcuts import render
import base64
from .models import Usuario, Blog, Contacto
import datetime

    # TODA ACCION PARTE DE UNA PETICION (INGRESO DE DATOS)
    # VISUALIZAR TODO (SELECT * FROM TABLA -> SELECCIONA TODOS LOS ELEMENTOS DE UNA TABLA) ((NO RECIBE PARAMETROS))
    # VISUALIZAR ELEMENTO O CIERTOS ELEMENTOS (SELECT * FROM  TABLA WHERE codicion = value)  ((RECIBE PARAMETROS value))
    # REGISTRO (RECIBE TODOS LOS PARAMETROS PARA REGISTRO)
    # ACTUALIZACION (RECIBE TODOS LOS PARAMETROS PARA ACTUALIZAR)
    # ELIMINACION (RECIBE EL PARAMETRO DEL REGISTRO A ELIMINAR) 

# Paginas de Admin

def adminPerfil(request):
    return render(request, 'admin/perfil.html')

def adminMensajes(request):
    return render(request, 'admin/mensajes.html')

def adminPublicaciones(request):
    return render(request, 'admin/publicaciones.html')

def mostrarRecepcionMensaje(request):
    mensajes = Contacto.objects.all()
    return render(request, 'admin/message.html', {'mensajes': mensajes})

def adminBlog(request):
    blogs = Blog.objects.all()
    return render(request, 'admin/blog.html',  {'blogs': blogs})



 

# Registros

def registrarUsuario(request):
    name = request.POST['nombre_usuario']
    email = request.POST['email_usuario']
    password = request.POST['password_usuario']
    imagen = request.FILES['imagen_usuario'].read()
    imagenb64 = request.POST['imagenstr']

    nuevoUsuario = Usuario(name = name, email = email, password = password, imagen = imagenb64)

    nuevoUsuario.save()
    return render(request, 'pages/registro.html')

def ingresarUsuario(request):
    # RECEPCION DE DATOS - INGRESO DE DATOS
    # PROCESO (BUSQUEDA DE DATOS - ACCION EN LA BASE DATOS (ELIMINAR, GUARDAR, EDITAR))
    # RETORNA EL RESULTADO ESPERADO

    # RECEPCION DE DATOS - INGRESO DE DATOS
    usuario_ingresado = request.POST['usuarioLogin']
    pass_ingresado = request.POST['passLogin']

    # PROCESO (BUSQUEDA DE DATOS - ACCION EN LA BASE DATOS (ELIMINAR, GUARDAR, EDITAR))
    itemUsuario = Usuario.objects.filter(name = usuario_ingresado)[0]
    if itemUsuario.password != pass_ingresado:
        itemUsuario = None

    # SELECT * FROM Usuario WHERE name = usuario_ingresado and password = pass_ingresado

    if (itemUsuario is None):
        
        return render(request, 'pages/errorSession.html')
        
    else:
        request.session['user_session'] = itemUsuario.name
        request.session['user_imagen'] = itemUsuario.imagen
        request.session['user_id'] = itemUsuario.id

        return render(request, 'pages/index.html')
        

    # RETORNA EL RESULTADO ESPERADO
    return render(request, 'pages/index.html')
    
def cerrarSession(request):
    request.session['user_session'] = None
    request.session['user_imagen'] = None
    request.session['user_id'] = None

    return render(request, 'pages/index.html')

def registrarBlog(request):
    titulo = request.POST['detalle_titulo']
    imagen = request.FILES['detalle_imagen'].read()
    imagenb64 = request.POST['detalle_imagen_str']
    introduccion = request.POST['detalle_introduccion']
    contenido = request.POST['detalle_contenido']
    fecha = datetime.datetime.now()
    usuario = Usuario.objects.get(id = int(request.session['user_id']))

    nuevoBlog = Blog (titulo = titulo, imagen = imagenb64, introduccion = introduccion, contenido = contenido,
    fecha = fecha, usuario_id = usuario)

    nuevoBlog.save()
    return render(request, 'admin/blog.html')

def eliminarBlog(request, idBlog):
    deleteBlog = Blog.objects.get(id = int(idBlog))
    deleteBlog.delete()
    return adminBlog(request)

def edicionBlog(request):
    blogEdicion = Blog.objects.get(id = int(request.POST['idBlog']))

    blogEdicion.titulo = request.POST['detalle_titulo']
    blogEdicion.imagen = request.POST['detalle_imagen_str']
    blogEdicion.introduccion = request.POST['detalle_introduccion']
    blogEdicion.contenido = request.POST['detalle_contenido']
    blogEdicion.fecha = datetime.datetime.now()

    blogEdicion.save()

    return render(request, 'admin/blog.html')


def mostrarEdicionBlog(request, idBlog):
    edicionBlog = Blog.objects.get(id = int(idBlog))
    blogs = Blog.objects.all()

    return render(request, 'admin/editarBlog.html', {'blog': edicionBlog, 'blogs' : blogs})

def enviarContacto(request):
    name = request.POST['detalle_nombre']
    email = request.POST['detalle_email']
    telefono = request.POST['detalle_telefono']
    motivo = request.POST['detalle_motivo']
    mensaje = request.POST['detalle_mensaje']
    fecha = datetime.datetime.now()
    usuario = Usuario.objects.get(id = int(request.session['user_id']))

    nuevoMensaje = Contacto (name = name, email = email, telefono = telefono, motivo = motivo,
    mensaje = mensaje, usuario = usuario)

    nuevoMensaje.save()
    return render(request, 'pages/sendMessage.html')


# Paginas Principales

def mostrarIndex(request):
    return render(request, 'pages/index.html')

def mostrarBlog(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/blog.html', {'blogs': blogs})

def verDetalleBlog(request, blogId):
    infoBlog = Blog.objects.get(id = int(blogId))
    return render(request, 'pages/blogDetalle.html', {'blog': infoBlog})

def mostrarDetalleBlog(request, blogId):
    infoBlog = Blog.objects.get(id = int(blogId))
    return render(request, 'pages/blogDetalle.html', {'blog': infoBlog})



def mostrarRegistro(request):
    return render(request, 'pages/registro.html')

def mostrarAbout(request):
    return render(request, 'pages/about.html')


def mostrarContact(request):
    return render(request, 'pages/contact.html')

def mostrarMessage(request):
    return render(request, 'pages/message.html')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('usuario')
            contraseña = form.cleaned_data.get('contraseña')

            user = authenticate(usuario=usuario, contraseña=contraseña)

            if user is not None:
                login(request,user)

                return render(request, 'pages/index.html')

            else:
                return render(request, 'pages/index.html')

        else:
            return render(request, 'pages/index.html')
    
    form = AuthenticationForm()

    return render(request, 'pages/index.html', {'form' : form})
