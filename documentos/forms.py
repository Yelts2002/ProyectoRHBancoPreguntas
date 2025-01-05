from django import forms
from .models import Universidad, Curso, Tema, Pregunta

class UniversidadForm(forms.ModelForm):
    class Meta:
        model = Universidad
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre de la Universidad',
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'universidad']
        labels = {
            'universidad': 'Universidad a la que Pertenece el Curso',
            'nombre': 'Nombre del Curso',

        }

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['nombre', 'nivel', 'curso']
        labels = {
            'nombre': 'Nombre del Tema',
            'curso': 'Curso al que pertenece el Tema'
        }

class PreguntaForm(forms.ModelForm):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=True)
    tema = forms.ModelChoiceField(queryset=Tema.objects.none(), required=True)  # Inicialmente vacío

    class Meta:
        model = Pregunta
        fields = ['contenido', 'universidad', 'curso', 'tema']  # Asegúrate de incluir todos los campos necesarios

    def __init__(self, *args, **kwargs):
        super(PreguntaForm, self).__init__(*args, **kwargs)
        if 'curso' in self.data:
            try:
                curso_id = int(self.data.get('curso'))
                self.fields['tema'].queryset = Tema.objects.filter(curso_id=curso_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # Si el curso no es válido, no se filtra
        elif self.instance.pk:
            self.fields['tema'].queryset = self.instance.curso.tema_set.order_by('nombre')