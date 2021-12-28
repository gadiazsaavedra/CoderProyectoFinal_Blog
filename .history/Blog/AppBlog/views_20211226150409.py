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
        miFormulario = BlogFormulario(initial={'title': Blog.title, 'numero': Blog.numero, 'esBueno': Blog.esBueno})
        
        
    return render(request, 'AppBlog/editarBlog.html', {'miFormulario': miFormulario,"numero_para_editar": numero_para_editar})

def eliminarBlog(request, numero_para_borrar):
    BlogQueQuieroBorrar = Blog.objects.get(numero=numero_para_borrar)
    BlogQueQuieroBorrar.delete()
    Blogs = Blog.objects.all()
    return render(request, 'AppBlog/leerBlogs.html', {'Blogs': Blogs})

@login_required
def leerBlogs(request):
    Blogs = Blog.objects.all()
    dic = {"Blogs": Blogs}
    return render(request, "AppBlog/leerBlogs.html", dic)

def busquedaConyuge(request):
    return render(request, 'AppBlog/busquedaConyuge.html')

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        conyuge = Conyuge.objects.filter(nombre__icontains=nombre)
    
        return render(request, 'AppBlog/resultadoBusqueda.html', {'conyuge': conyuge, 'nombre': nombre})
    else:
        respuesta = "Por favor ingresar un nombre"
        #respuesta = f"Estoy buscando la conyuge de nombre : {request.GET['nombre']}"
    return HttpResponse(respuesta)
# Create your views here.
def  abuelosFormulario(request):
    if request.method == 'POST':
        miFormulario = AbuelosFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                abuelos = Abuelos(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'])               
                abuelos.save()
                return render(request, 'AppBlog/inicio.html')
    else:
        miFormulario = AbuelosFormulario()
        
        
    return render(request, 'AppBlog/abuelosFormulario.html', {'miFormulario': miFormulario})

def  primoFormulario(request):
    if request.method == 'POST':
        miFormulario = PrimoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                prim = Primo(nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'], profesional=informacion['profesional'], fechaDeNacimiento=informacion['fechaDeNacimiento'])               
                prim.save()
                return render(request, 'AppBlog/inicio.html')
    else:
        miFormulario = PrimoFormulario()
        
        
    return render(request, 'AppBlog/primoFormulario.html', {'miFormulario': miFormulario})

def BlogFormulario(request):
    if request.method == 'POST':
        miFormulario = BlogFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                hij = Blog(
                    apellido=informacion['apellido'],
                    numero=informacion['numero'],
                    esBueno=informacion['esBueno'])               
                hij.save()
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
