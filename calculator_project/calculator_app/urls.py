from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='home'),
    path('calculator/', views.calculator, name='calculator'),
     path('calculator_get/', views.calculator_get, name='calculator_get'),
]

