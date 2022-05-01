"""proyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from appAdministracionBlog import views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

urlpatterns = [
    path('admin/', include('appAdministracionBlog.urls'), name = 'admin'),
    path('index/', views.mostrarIndex),
    path('blog/', views.mostrarBlog),
    path('detalleBlog/<blogId>', views.mostrarDetalleBlog),
    path('registro/', views.mostrarRegistro),
    path('about/', views.mostrarAbout),
    path('contact/', views.mostrarContact),
    path('message/', views.mostrarMessage),
    path('blog/<blogId>', views.verDetalleBlog),
    path('eliminarBlog/', views.eliminarBlog, name = 'eliminarBlog'),
    path('ingresoUsuario/', views.ingresarUsuario, name = 'ingresarUsuario'),
    path('cerrarSession/', views.cerrarSession, name = 'cerrarSession'),
    path('enviarContacto/', views.enviarContacto, name = 'enviarContacto'),
  

    # path('login', views.login_request, name = 'login'),

    
    
    
]
