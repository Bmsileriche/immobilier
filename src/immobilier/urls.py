
from django.contrib import admin
from django.urls import path
from client import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('client/', views.index,),
    path('client/add/', views.add, name='add'),
    path('client/', views.afficher_clients, name='afficher_clients'),
    path(
    'client/supprimer_client/<int:id>/',views.supprimer_client, name='supprimer_client'),
   
     
]
