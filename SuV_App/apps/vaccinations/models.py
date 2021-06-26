from django.db import models
from patients.models import Patient
from vaccines.models import Vaccine
from posto.models import Posto
from employees.models import Employee

# Create your models here.

class Vaccination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE)
    observation = models.TextField('Observação', max_length=200)
    date_vaccination = models.DateField('Data de Aplicação', auto_now=False, auto_now_add=False)
             
    class Meta:
        verbose_name = 'Vacinação'
        verbose_name_plural = 'Vacinacao'
        ordering =['id']

    def __str__(self):
        return self.product.name
