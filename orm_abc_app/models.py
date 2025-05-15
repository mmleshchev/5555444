# models.py
from django.db import models

class Admission(models.Model):
    full_name      = models.CharField("ФИО", max_length=255)
    admission_year = models.PositiveIntegerField("Год поступления")
    program_name   = models.CharField("Название ОП", max_length=255)
    date_submitted = models.DateTimeField("Дата заполнения", auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.admission_year})"
