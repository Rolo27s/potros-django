from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from potros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Página inicial
    path('noticias/', views.get_all_noticias, name='noticias'),
    path('calendario/', views.get_calendario, name='calendario'),
    path('equipo/', views.get_equipo, name="equipo"),
    path('instagram/', views.get_instagram, name="instagram")
]

# Necesario para un correcto acceso a la carpeta de media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
