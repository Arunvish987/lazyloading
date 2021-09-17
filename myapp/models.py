from django.db import models

# Create your models here.

class Number(models.Model):
    numbers = models.IntegerField()
    words = models.CharField(max_length=50)

    def __str__(self):
        return str(self.number)
    
