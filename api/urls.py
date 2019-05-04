from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('food/', views.inventory),
    path('image/',views.images),
]