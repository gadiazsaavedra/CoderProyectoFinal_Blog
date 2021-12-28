from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('inicio', views.inicio, name='Inicio'),
    path('blogs', views.blogs, name='Blogs'),
    path('blogFormulario', views.blogFormulario, name='BlogFormulario'),
    path('leerBlogs', views.leerBlogs, name='LeerBlogs'),
    path('eliminarBlog/numero_para_borrar', views.eliminarBlog, name='EliminarBlog'),
    path('editarBlog/numero_para_editar', views.editarBlog, name='EditarBlog'),
    
    path('blogger/list', views.BloggerList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.bloggerDetalle.as_view(), name='Detail'),
    
    
    path(r'^nuevo$', views.bloggerCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.bloggerUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.bloggerDelete.as_view(), name='Delete'),
    
    
    
    #Clase 23 LOGIN
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppFamiliar/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),

    
    
    
    
    path('blogger/', views.blogger_list, name='blogger_list'),
    path('blogger/<int:pk>/', views.blogger_detail, name='blogger_detail'),
    path('blogger/new/', views.blogger_new, name='blogger_new'),
    path('blog/', views.blog, name='blog'),
               
               
]