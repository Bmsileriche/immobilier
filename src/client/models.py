from django.db import models



# Create your models here.
class Client(models.Model):
    SEXE_CHOICES = [
        ('M','M.'),
        ('Mme','Mme'),

    ]
    nom = models.CharField(max_length=100)
    prenom= models.CharField(max_length=100)
    numero= models.CharField(max_length=20)
    email= models.EmailField()
    sexe = models.CharField(
        max_length=3,
        choices=SEXE_CHOICES
    
        )
