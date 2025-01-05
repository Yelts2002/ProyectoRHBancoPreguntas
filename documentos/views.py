from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UniversidadForm, CursoForm, TemaForm, PreguntaForm
from .models import Universidad, Curso, Tema, Pregunta



def home(request):
    return redirect('cargar_documento')  # Redirige a la vista de cargar documento

## Vista para subir el documento(pregunmta)
def cargar_documento(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST, request.FILES)
        if form.is_valid():
            pregunta = form.save(commit=False)  # No guardar aún en la base de datos

            # Obtener los datos del formulario
            curso = form.cleaned_data['curso']  # Acceder al curso desde cleaned_data
            tema = form.cleaned_data['tema']      # Acceder al tema desde cleaned_data
            universidad = form.cleaned_data['universidad']  # Acceder a la universidad desde cleaned_data

            # Generar el nombre del contenido
            curso_nombre = curso.nombre.replace(" ", "_")  # Reemplazar espacios por guiones bajos
            tema_nombre = tema.nombre.replace(" ", "_")
            universidad_nombre = universidad.nombre[:3].upper()  # Tomar las primeras 3 letras de la universidad

            # Contar preguntas existentes para el curso y tema
            pregunta_count = Pregunta.objects.filter(tema=tema, universidad=universidad).count() + 1  # Contar preguntas existentes

            # Crear el nombre del contenido
            contenido_nombre = f"{curso_nombre}_{tema_nombre}_{universidad_nombre}_preg{pregunta_count}"
            pregunta.contenido = contenido_nombre  # Asignar el nombre al campo contenido

            pregunta.save()  # Ahora guardar en la base de datos
            return redirect('listar_preguntas')  # Cambia esto según tu lógica
    else:
        form = PreguntaForm()
    return render(request, 'cargar_documento.html', {'form': form})
def get_temas(request, curso_id):
    temas = Tema.objects.filter(curso_id=curso_id).values('id', 'nombre')
    return JsonResponse({'temas': list(temas)})

# Vista para gestionar universidades, cursos y temas
def gestionar_universidades_cursos_temas(request):
    universidades = Universidad.objects.all()
    cursos = Curso.objects.all()
    temas = Tema.objects.all()

    if request.method == 'POST':
        # Manejar la creación de universidades, cursos y temas
        if 'crear_universidad' in request.POST:
            form_universidad = UniversidadForm(request.POST)
            if form_universidad.is_valid():
                form_universidad.save()
                return redirect('gestionar_universidades_cursos_temas')

        elif 'crear_curso' in request.POST:
            form_curso = CursoForm(request.POST)
            if form_curso.is_valid():
                form_curso.save()
                return redirect('gestionar_universidades_cursos_temas')

        elif 'crear_tema' in request.POST:
            form_tema = TemaForm(request.POST)
            if form_tema.is_valid():
                form_tema.save()
                return redirect('gestionar_universidades_cursos_temas')

    else:
        form_universidad = UniversidadForm()
        form_curso = CursoForm()
        form_tema = TemaForm()

    context = {
        'universidades': universidades,
        'cursos': cursos,
        'temas': temas,
        'form_universidad': form_universidad,
        'form_curso': form_curso,
        'form_tema': form_tema,
    }
    return render(request, 'gestionar_universidades_cursos_temas.html', context)

# Vista para listar preguntas
def listar_preguntas(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'listar_preguntas.html', {'preguntas': preguntas})

# Vista para ver datos de las tablas
def ver_datos_tablas(request):
    universidades = Universidad.objects.all()
    cursos = Curso.objects.all()
    temas = Tema.objects.all()
    preguntas = Pregunta.objects.all()

    context = {
        'universidades': universidades,
        'cursos': cursos,
        'temas': temas,
        'preguntas': preguntas,
    }
    return render(request, 'ver_datos_tablas.html', context)