from django.urls import path
from .views import (
    home,
    cargar_documento,
    gestionar_universidades_cursos_temas,
    listar_preguntas,
    ver_datos_tablas,
    get_temas,  # Importa la nueva vista

)

urlpatterns = [
    path('', home, name='home'),  # Página de inicio
    path('documentos/cargar/', cargar_documento, name='cargar_documento'),
    path('gestionar/', gestionar_universidades_cursos_temas, name='gestionar_universidades_cursos_temas'),
    path('listar_preguntas/', listar_preguntas, name='listar_preguntas'),
    path('ver_datos_tablas/', ver_datos_tablas, name='ver_datos_tablas'),
    path('get_temas/<int:curso_id>/', get_temas, name='get_temas'),  # Nueva URL para obtener temas

]