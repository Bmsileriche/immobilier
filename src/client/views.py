from django.shortcuts import render, redirect
from .models import Client

# Afficher la liste des clients
def afficher_clients(request):
    clients = Client.objects.all().order_by('id')
    return render(request, "client/accueil.html", {"clients": clients})

# ajouter un client dans la liste
def add(request):
    if request.method == "POST":
        Client.objects.create(
            nom=request.POST["nom"],
            prenom=request.POST["prenom"],
            numero=request.POST["numero"],
            email=request.POST["email"],
            sexe=request.POST["sexe"],
        )

        return redirect("afficher_clients")

    return render(request, "client/accueil.html")

# supprimer client dans la liste
def supprimer_client(request, id):
    client = Client.objects.get( id=id)

    client.delete()

    return redirect('afficher_clients')
    




