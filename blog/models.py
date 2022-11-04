from django.contrib.auth.models import User
from django.db import models

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveIntegerField()
    kasb = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):return f"{self.ism}"

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateField()
    mavzu = models.CharField(max_length=50)
    matn = models.CharField(max_length=100)
    muallif = models.OneToOneField(Muallif, on_delete=models.CASCADE)
    def __str__(self):return f"{self.sarlavha}"