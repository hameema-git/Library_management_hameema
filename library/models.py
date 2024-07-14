from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    language=models.CharField(max_length=50)
    price=models.FloatField()
    rating=models.IntegerField()
    def __str__(self):
        return self.name

