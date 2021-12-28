from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('blogger/', views.blogger_list, name='blogger_list'),
    path
               
               
               ]