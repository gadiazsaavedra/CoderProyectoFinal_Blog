from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from AppBlog.models import Blog, Blogger
from AppBlog.forms import BlogForm, BloggerForm
#para el login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def editBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Guardado')
    else:
        form = BlogForm()
    return render(request, 'blog/editBlog.html', {'form': form})

def deleteBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Guardado')
    else:
        form = BlogForm()
    return render(request, 'blog/deleteBlog.html', {'form': form})

def createBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Guardado')
    else:
        form = BlogForm()
    return render(request, 'blog/createBlog.html', {'form': form})

def updateBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Guardado')
    else:
        form = BlogForm()
    return render(request, 'blog/updateBlog.html', {'form': form})

def listBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Guardado')
    else:
        form = BlogForm()
    return render(request, 'blog/listBlog.html', {'form': form})

def inicio(request):
    return render(request, 'AppBlog/index.html')

def blogger(request):
    return render(request, 'AppBlog/blogger.html')

def blog(request):
    return render(request, 'AppBlog/blog.html')

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView