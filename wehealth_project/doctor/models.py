from django.db import models

# Create your models here.
class Doctor(models.Model):
    consultation_fee = models.IntegerField(default=100)
    username = models.CharField(max_length=20)
    max_appointments = models.IntegerField()
    
    def __str__(self) -> str:
        return self.username