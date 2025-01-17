
from django.db import models

# Create your models here.


    
class PortfolioProduit(models.Model):
    nom=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='produits',blank=True,null=True)

class PortfolioService(models.Model):
    nom=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='services',blank=True,null=True)
    
class PortfolioExperts(models.Model):
    nom=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='experts',blank=True,null=True)    


    
class Reservations (models.Model):
    username=models.CharField(max_length=500)
    email=models.EmailField(default=True)
    
   