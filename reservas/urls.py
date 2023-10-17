
from django.contrib import admin
from django.urls import include, path
from reservas.views import Cadastrar, Apagar, Listar, Editar,  Index, Nos, Mais,Detalhar, Index_nao, perfil,a
from django.conf.urls.static import static
from django.conf import settings

app_name = "reservas"

urlpatterns = [
    path('accounts/', include('allauth.urls')), 
    
    path('admin/', admin.site.urls),
    path('index/', Index.as_view(),name='index'),
    path('sobre/', a.as_view(),name='a'),
    path('perfil/', perfil.as_view(), name='perfil'),
    path('mais/',Mais.as_view(), name='mais'),
    path('', Index_nao.as_view(), name='index_nao'),
    path('sobre_nos/', Nos.as_view(), name='nos'),
    
    path('form/', Cadastrar.as_view(),name='cadastrar'),
    path('listar/', Listar.as_view(),name='listar'),
    path('editar/<int:pk>/', Editar.as_view(), name='editar'),
    path('apagar/<int:pk>/',Apagar.as_view(), name='apagar'),
    path('detalhar/<int:pk>/', Detalhar.as_view(), name='detalhar'),
    
    #login
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)