from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.say_hello),
    path('temp/', views.tem_func),
    path('hello2/', views.say_hello2),
    path('shcart/', views.shopCart)
]
