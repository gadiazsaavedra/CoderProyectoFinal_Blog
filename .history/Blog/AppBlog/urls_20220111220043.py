from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('inicio', views.inicio, name='Inicio'),
    path('posteos', views.posteos, name='Posteos'),
    path('posteoFormulario', views.posteoFormulario, name='PosteoFormulario'),
    path('leerPosteos', views.leerPosteos, name='LeerPosteos'),
    path('eliminarPosteo/<numero_para_borrar>/', views.eliminarPosteo, name='EliminarPosteo'),
    path('editarPosteo/>numero_para_editar>/', views.editarPosteo, name='EditarPosteo'),
    path('posteoFormulario', views.posteoFormulario, name='PosteoFormulario'),
    
    path('usuario/list', views.UsuarioList.as_view(), name='List'),
    path('usuario_detail', views.UsuarioDetail.as_view(), name='Detail'),
    path('usuario_form', views.UsuarioCreacion.as_view(), name='New'),
    path(r'^nuevo$', views.UsuarioCreacion.as_view(), name='New1'),
    path('usuario_confirm_delete', views.UsuarioUpdate.as_view(), name='Edit'),
    #path('usuario_confirm_delete', views.UsuarioDelete.as_view(), name='Delete'),
    
    
    
    #Clase 23 LOGIN
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
    path('about', views.about, name="About"),
    path('post', views.post, name="Post"),
    path('contact', views.contact, name="Contact"),
    
    
               
]