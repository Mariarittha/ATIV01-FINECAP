from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from .models import Reserva,Stand
from .forms import ReservaForm,StandForm
from  django.contrib.auth import authenticate
from  django.contrib.auth import login as loginho
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages import views

class Index(generic.TemplateView):
    template_name = "reservas/index.html"
    
class Mais(generic.TemplateView):
    template_name = "reservas/mais.html"
    
class Nos(generic.TemplateView):
    template_name = "reservas/nos.html"
    
class Detalhar(DetailView):
    model = Reserva
    template_name = "reservas/detalhar.html"  
    context_object_name = 'reservas'

 
class Listar(ListView):
    template_name = "reservas/listar.html"
    model = Reserva
    context_object_name = 'reservas'

class Cadastrar(views.SuccessMessageMixin, generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  template_name = "reservas/form.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva cadastrada com sucesso!"
  
class Apagar(views.SuccessMessageMixin, generic.DeleteView):
  model = Reserva
  template_name = "reservas/apagar.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva removida com sucesso!"
  
class Editar(views.SuccessMessageMixin, generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  template_name = "reservas/form.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva atualizada com sucesso! " 
  
  def login(request):
     if request.method == 'GET':
         return render(request, 'Restrito/login.html')
     else:
         username = request.POST.get('username')
         senha = request.POST.get('senha')
        
         user = authenticate(username = username, password = senha)
        
         if user:
             loginho(request, user)
             return redirect('listar')
         else:
              messages.error(request,'username ou senha inválida') 
         return redirect('login')
     

