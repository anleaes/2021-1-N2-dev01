from django.db import models
from categories.models import Category

# Create your models here.


class Vaccine(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField(
        'Data Fabricacao', auto_now=False, auto_now_add=False)
    expiration_date = models.DateField(
        'Data Vencimento', auto_now=False, auto_now_add=False)
    is_active = models.BooleanField('Ativo', default=False)
    photo = models.ImageField('Foto', upload_to='photos')
    doc = models.FileField('Documentos', upload_to='docs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering = ['id']

    def __str__(self):
        return self.name
