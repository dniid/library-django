from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name = 'bread'),
    path('create/', views.create, name = 'book_create'),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete)
]
