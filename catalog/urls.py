from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name = 'cread'),
    path('create/', views.create, name = 'catalog_create'),
    path('update/<int:id>', views.update, name = 'catalog_update'),
    path('delete/<int:id>', views.delete, name = 'catalog_delete'),
]
