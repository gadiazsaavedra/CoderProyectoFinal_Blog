from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from AppBlog.models import Blog, Bloggers
from AppBlog.forms import PosteoFormulario, UsuarioFormulario, UserRegisterForm, UserEditForm
#para el login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.views.generic.detail import DetailView

from django.views import generic
from .models import Blog




# Create your views here.
def editarPosteo(request, numero_para_editar):
    posteo = Posteo.objects.get(numero=numero_para_editar)
    if request.method == 'POST':
        miFormulario = Formulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                posteo.titulo = informacion['titulo']
                posteo.numero = informacion['numero']
                posteo.descripcion = informacion['descripcion']
                posteo.usuario = informacion['usuario']
                posteo.creado = informacion['creado']
                posteo.actualizado = informacion['actualizado']
                posteo.save()
                return render(request, 'AppBlog/inicio.html')
    else:
        miFormulario = PosteoFormulario(initial={'titulo': posteo.titulo, 'numero':posteo.numero, 'descripcion': posteo.descripcion, 'usuario': posteo.usuario, 'creado': posteo.creado, 'actualizado': posteo.actualizado})
        
        
    return render(request, 'AppBlog/editarBlog.html', {'miFormulario': miFormulario, "numero_para_editar":numero_para_editar})

def eliminarPosteo(request, numero_para_borrar):
    posteoQueQuieroBorrar = Posteo.objects.get(numero=numero_para_borrar)
    posteoQueQuieroBorrar.delete()
    posteos = Posteo.objects.all()
    return render(request, 'AppBlog/leerBlogs.html', {'posteos': posteos})


def leerPosteos(request):
    posteos = Posteo.objects.all()
    dic = {"blogs": blogs}
    return render(request, "AppBlog/leerBlogs.html", dic)



def posteoFormulario(request):
    if request.method == 'POST':
        miFormulario = PosteoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                pos = Posteo(
                    titulo=informacion['titulo'],
                    descripcion=informacion['descripcion'],
                    usuario=informacion['usuario'],
                    creado=informacion['creado'],
                    actualizado=informacion['actualizado'])               
                pos.save()
                return render(request, 'AppBlog/inicio.html')
    else:
            miFormulario = PosteoFormulario()
    return render(request, 'AppBlog/posteoFormulario.html',{"miFormulario":miFormulario})

def inicio(request):
    return render(request, 'AppBlog/inicio.html')

def posteos(request):
    return render(request, 'AppBlog/blogs.html')

def about(request):
    return render(request, 'AppBlog/about.html')

def post(request):
    return render(request, 'AppBlog/post.html')

def contact(request):
    return render(request, 'AppBlog/contact.html')


from django.views.generic import ListView

from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView



#Leer --- nos da todos los padres
class UsuarioList(ListView):
    
    model = 
    template_name = "AppBlog/bloggers_list.html"
    
#Detalle - SUPER Leer - Buscar!!!!!
class UsuarioDetail(DetailView):
    
    model = Usuario
    template_name = "AppBlog/blogger_detail.html"
    
#Crear elementos
class UsuarioCreacion(CreateView):
    
    model = Usuario
    success_url = "../usuario/list"
    fields = ["name", "email", "phone", "address", "city", "state", "zip", "website", "company", "about", "created_at", "updated_at"]
    
#modificar!!!!!!!!!!!  
class UsuarioUpdate(UpdateView):
    
    model = Usuario
    success_url = "../usuario/list"
    fields = ["name", "email", "phone", "address", "city", "state", "zip", "website", "company", "about", "created_at", "updated_at"]
  
#Borrar   
class BloggerDelete(DeleteView):
    
    model = Usuario
    success_url = "../usuario/list"
    
    

def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "AppBlog/inicio.html", {"mensaje":f"BIENVENIDO al BLOG : {usuario}  !!!!"})
                
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


