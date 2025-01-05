from django.db import models

class Universidad(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Tema(models.Model):
    nombre = models.CharField(max_length=255)
    nivel = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    contenido = models.FileField(upload_to='documentos/')
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenido.name