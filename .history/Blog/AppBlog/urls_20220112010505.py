from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('inicio', views.inicio, name='Inicio'),
    #path('blogs', views.blogs, name='Blogs'),
    path('blogFormulario', views.blogFormulario, name='BlogFormulario'),
    path('leerBlogs', views.leerBlogs, name='LeerBlogs'),
    path('eliminarBlog/<numero_para_borrar>/', views.eliminarBlog, name='EliminarBlog'),
    path('editarBlog/<numero_para_editar>/', views.editarBlog, name='EditarBlog'),
    
    
    path('blogger/list', views.BloggerList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.BloggerDetail.as_view(), name='Blogger_detail'),
    path(r'^nuevo$', views.BloggerCreacion.as_view(), name='New'),
    path('blogger_confirm_delete', views.BloggerUpdate.as_view(), name='Edit'),
    path('blogger_confirm_delete', views.BloggerDelete.as_view(), name='Delete'),
    
    
    
    #Clase 23 LOGIN
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
    path('about', views.about, name="About"),
    path('post', views.post, name="Post"),
    path('contact', views.contact, name="Contact"),
    
    
               
]