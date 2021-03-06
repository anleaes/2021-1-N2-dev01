from django.db import models

# Create your models here.

class Posto(models.Model):
    posto_name = models.CharField('Nome', max_length=50)
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    
    class Meta:
        verbose_name = 'Posto'
        verbose_name_plural = 'Postos'
        ordering =['id']

    def __str__(self):
        return self.posto_name