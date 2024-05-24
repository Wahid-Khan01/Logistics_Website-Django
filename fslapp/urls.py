from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/about', views.about, name='about'),
    path('/fcl', views.fcl, name='fcl'),
    path('/lcl', views.lcl, name='lcl'),
    path('/airfreight', views.airfreight, name='airfreight'),
    path('/customclearance', views.customclearance, name='customclearance'),
    path('/industries', views.industries, name='industries')
]