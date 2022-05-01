from django.shortcuts import render


def mostrarMaster(request):

    return render(request, 'masterPage.html')

def mostrarBlog(request):

    return render(request, 'pages/blog.html')


def mostrarDetalleBlog(request):

    return render(request, 'pages/blogDetalle.html')


def adminPerfil(request):

    return render(request, 'admin/perfil.html')

def mostrarDetalleBlog(request):

    return render(request, 'pages/blogDetalle.html')