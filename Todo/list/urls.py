from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_item, name='list'),
    path('delete/<int:item_id>/', views.delete_item)
]