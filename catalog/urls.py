from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name = 'read'),
    path('create/', views.create, name = 'catalog_create'),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete)
]
