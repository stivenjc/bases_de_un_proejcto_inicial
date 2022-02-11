from django.db import models

# Create your models here.

class Comidas(models.Model):
    carne = models.CharField(max_length=200,)

    class Meta:
        db_table = 'comidass'

    def __str__(self):
        return self.carne

