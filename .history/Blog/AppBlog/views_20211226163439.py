from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from AppBlog.models import Blog, Blogger
from AppBlog.forms import BlogFormulario, BloggerFormulario
#para el login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def editarBlog(request, numero_para_editar):
    blog = Blog.objects.get(numero=numero_para_editar)
    if request.method == 'POST':
        miFormulario = BlogFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                blog.title = informacion['title']
                blog.numero = informacion['numero']
                blog.description = informacion['description']
                blog.blogger = informacion['blogger']
                blog.created_at = informacion['created_at']
                blog.updated_at = informacion['updated_at']
                blog.save()
                return render(request, 'AppBlog/inicio.html')
    else:
        miFormulario = BlogFormulario(initial={'title': blog.title, 'numero': blog.numero, 'description': blog.description, 'blogger': blog.blogger, 'created_at': blog.created_at, 'updated_at': blog.updated_at})
        
        
    return render(request, 'AppBlog/editarBlog.html', {'miFormulario': miFormulario,"numero_para_editar": numero_para_editar})

def eliminarBlog(request, numero_para_borrar):
    blogQueQuieroBorrar = Blog.objects.get(numero=numero_para_borrar)
    blogQueQuieroBorrar.delete()
    blogs = Blog.objects.all()
    return render(request, 'AppBlog/leerBlogs.html', {'blogs': blogs})


def leerBlogs(request):
    blogs = Blog.objects.all()
    dic = {"blogs": blogs}
    return render(request, "AppBlog/leerBlogs.html", dic)



def blogFormulario(request):
    if request.method == 'POST':
        miFormulario = BlogFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                blo = Blog(
                    title=informacion['title'],
                    numero=informacion['numero'],
                    description=informacion['description']),
                    blogger=informacion['blogger'],
                    created_at=informacion['created_at'],
                                   
                blo.save()
                return render(request, 'AppBlog/inicio.html')
    else:
            miFormulario = BlogFormulario()
    return render(request, 'AppBlog/BlogFormulario.html',{"miFormulario":miFormulario})

def inicio(request):
    return render(request, 'AppBlog/inicio.html')

def Blogs(request):
    return render(request, 'AppBlog/Blogs.html')

def conyuge(request):
    return render(request, 'AppBlog/conyuge.html')

from django.views.generic import ListView

from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView

#from django.urls import reverse_lazy

#Leer --- nos da todos los padres
class PadreList(ListView):
    
    model = Padre
    template_name = "AppBlog/padres_list.html"
    
#Detalle - SUPER Leer - Buscar!!!!!
class PadreDetalle(DetailView):
    
    model = Padre
    template_name = "AppBlog/padre_detalle.html"
    
#Crear elementos
class PadreCreacion(CreateView):
    
    model = Padre
    success_url = "../padre/list"
    fields = ["nombre", "apellido", "telefono", "direccion", "correo", "fecha_nacimiento", "parentesco"]
    
#modificar!!!!!!!!!!!  
class PadreUpdate(UpdateView):
    
    model = Padre
    success_url = "../padre/list"
    fields = ["nombre", "apellido", "telefono", "direccion", "correo", "fecha_nacimiento", "parentesco"]
  
#Borrar   
class PadreDelete(DeleteView):
    
    model = Padre
    success_url = "../padre/list"
    
    

def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "AppBlog/inicio.html", {"mensaje":f"BIENVENIDO, {usuario}!!!!"})
                
            else:
                
                return render(request, "AppBlog/inicio.html", {"mensaje":f"DATOS MALOS :(!!!!"})
                
            
        else:
            
            return render(request, "AppBlog/inicio.html", {"mensaje":f"FORMULARIO erroneo"})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "AppBlog/login.html", {"form":form} )

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                  
                  
                  form.save()
                  
                  return render(request,"AppBlog/inicio.html" ,  {"mensaje":f"{username} fue creado como usuario..!!"})

      else:
            #form = UserCreationForm()     
            
              
            form = UserRegisterForm()     

      return render(request,"AppBlog/register.html" ,  {"form":form})
  
@login_required
def editarPerfil(request):
    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()
            
             
            return render(request, "AppBlog/inicio.html")
            
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
    return render(request, "AppBlog/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})
