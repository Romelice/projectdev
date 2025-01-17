from django.shortcuts import render

from .models import PortfolioExperts, PortfolioProduit, PortfolioService, Reservations

# Create your views here.
from . import views 

def homeView(request):
    return render(request, "/home/anafatrar/Documents/project/project/cours/templates/cours/portfolio/cv.html")

# Create your views here.


def  portfolioView(request):
        pdt = PortfolioProduit.objects.all()
        pts= PortfolioService.objects.all()
        pte = PortfolioExperts.objects.all()
        context={
            'portfolioProduit':pdt,
             'portfolioservice':pts,
             'porfolioexperts':pte,
        }
        return render(request,"/home/anafatrar/Documents/project/project/cours/templates/cours/portfolio/portfolio.html",context)




def createView(request):
     
     message=''

     if request.method=="POST":

        data = request.POST
        username = data.get('username')
        email = data.get('email')
        Reservations.objects.create(username= username, email= email)

        message ='reservation a été bien enregistré'

     return render(request,'./cours/portfolio/portfoliocreate.html', {'message':message})


def  ReserveView(request):
    Reserve = Reservations.objects.all().order_by('id')
   
    context={
            'reserve':Reserve,
            
        }
    return render(request,"/home/anafatrar/Documents/project/project/cours/templates/cours/portfolio/reserve.html",context)


