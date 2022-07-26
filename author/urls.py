from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthorListView.as_view(), name = 'author_all'),
    path('create/', views.AuthorCreateView.as_view(), name = 'author_create'),
    path('update/<int:pk>', views.AuthorUpdateView.as_view(), name = 'author_update'),
    path('delete/<int:pk>', views.AuthorDeleteView.as_view(), name = 'author_delete')
]
