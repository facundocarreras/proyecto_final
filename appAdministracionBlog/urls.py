from django.contrib import admin
from django.urls import path
from appAdministracionBlog import views

urlpatterns = [
    path('perfil/', views.adminPerfil),
    path('blog/', views.adminBlog),

    # Registro

    path('registrarUsuario/', views.registrarUsuario, name = 'registrarUsuario'),
    path('registrarBlog/', views.registrarBlog, name = 'registrarBlog'),
    path('eliminarBlog/<idBlog>', views.eliminarBlog, name = 'eliminarBlog'),
    path('mostrarEdicionBlog/<idBlog>', views.mostrarEdicionBlog, name = 'mostrarEdicionBlog'),
    path('edicionBlog/', views.edicionBlog, name = 'edicionBlog'),
    path('mostrarRecepcionMensaje/', views.mostrarRecepcionMensaje, name = 'mostrarRecepcionMensaje'),
    
    
    
]