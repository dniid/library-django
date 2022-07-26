from django.urls import path
from . import views

urlpatterns = [
    path('', views.CatalogListView.as_view(), name = 'catalog_all'),
    path('create/', views.CatalogCreateView.as_view(), name = 'catalog_create'),
    path('update/<int:pk>', views.CatalogUpdateView.as_view(), name = 'catalog_update'),
    path('delete/<int:pk>', views.CatalogDeleteView.as_view(), name = 'catalog_delete')
]
