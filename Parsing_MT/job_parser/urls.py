from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('parser_app.urls')),  # Это направляет корневой URL на ваше приложение parser_app
]