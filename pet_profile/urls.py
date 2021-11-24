from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pet_id>/', views.pet, name="pet"),
    path('add/', views.add, name="add"),
]
