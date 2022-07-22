from django.contrib import admin
from django.urls import path, include
from menu.views import menuView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menuView),
    path('catalog/', include('catalog.urls'))
]