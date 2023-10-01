from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from .forms import StandForm
from reservas.models import Stand
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages import views


class Detalharstand(DetailView):
    model = Stand
    template_name = "stand/detalhar.html"  
    context_object_name = 'stands'

 
class Listar(ListView):
    template_name = "stand/listar.html"
    model = Stand
    context_object_name = 'stands'
    paginate_by = 3


class Cadastrar(views.SuccessMessageMixin, generic.CreateView):
  model = Stand
  form_class = StandForm
  template_name = "stand/form.html"
  success_url = reverse_lazy("stand:listarstand")
  success_message = "Stand cadastrada com sucesso!"
  
class Apagar(views.SuccessMessageMixin, generic.DeleteView):
  model = Stand
  template_name = "stand/apagar.html"
  success_url = reverse_lazy("stand:listarstand")
  success_message = "Stand removida com sucesso!"
  
class Editar(views.SuccessMessageMixin, generic.UpdateView):
  model = Stand
  form_class = StandForm
  template_name = "stand/form.html"
  success_url = reverse_lazy("stand:listarstand")
  success_message = "Stand atualizada com sucesso! " 
  


# class StandsListView(generic.ListView):
#     model = Stand
#     paginate_by = 3

# class StandDetailView(generic.DetailView):
#     model = Stand

# class StandCreateView(views.SuccessMessageMixin, generic.CreateView):
#     model = Stand
#     form_class = StandForm
#     template_name = 'stand/form.html'
#     success_url = reverse_lazy("stands:stands-list")
#     success_message = "Stand cadastrado com sucesso!"

# class StandUpdateView(views.SuccessMessageMixin, generic.UpdateView):
#     model = Stand
#     form_class = StandForm
#     success_url = reverse_lazy("stands:stands-list")
#     success_message = "Stand atualizada com sucesso!"

# class StandDeleteView(generic.DeleteView):
#     model = Stand
#     success_url = reverse_lazy("stands:stands-list")