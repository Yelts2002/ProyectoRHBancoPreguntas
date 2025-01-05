from django.contrib import admin
from django.urls import path, include
from documentos.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documentos/', include('documentos.urls')),  # Incluye las URLs de la aplicación 'documentos'
    path('', home, name='home'),  # Elimina o comenta esta línea si no tienes la vista 'home'

]
