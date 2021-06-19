from django.db import models
from patients.models import Patient
from vaccines.models import Vaccine

# Create your models here.

class Vaccination(models.Model):
    quantity = models.IntegerField('Quantidade',null=True, blank=True)
    price = models.FloatField('Preco',null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Vacinação'
        verbose_name_plural = 'Vacinações'
        ordering =['id']

    def __str__(self):
        return self.product.name
