from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('inicio', views.inicio, name='Inicio'),
    path('blogs', views.blogs, name='Blogs'),
    path
    
    path('blogger', views.blogger, name='blogger'),
    path('blogger/', views.blogger_list, name='blogger_list'),
    path('blogger/<int:pk>/', views.blogger_detail, name='blogger_detail'),
    path('blogger/new/', views.blogger_new, name='blogger_new'),
    path('blog/', views.blog, name='blog'),
               
               
]