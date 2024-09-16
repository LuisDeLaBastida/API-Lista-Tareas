from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)  # Título de la tarea
    description = models.TextField()  # Descripción de la tarea
    completed = models.BooleanField(default=False)  # Si la tarea está completada

    def __str__(self):
        return self.title
