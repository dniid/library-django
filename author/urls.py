from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name = 'aread'),
    path('create/', views.create, name = 'author_create'),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete)
]
