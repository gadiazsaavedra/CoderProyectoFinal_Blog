from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from AppBlog.models import Blog, Blogger
from AppBlog.forms import BlogForm, BloggerForm
#para el login
from django.contrib.auth.forms import Authen

# Create your views here.
