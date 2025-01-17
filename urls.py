from django.urls import path

from .import views

urlpatterns = [
   path('',views.homeView,name="home"),
   path('portfolio/',views.portfolioView,name='portfolio'),
   path('portfoliocreate/',views.createView,name='portfoliocreate'),
   path('reserve/',views.ReserveView,name="reserve")
  # path('portfolioForm/',views.PortfolioformView,name='portfolioForm')
   ]