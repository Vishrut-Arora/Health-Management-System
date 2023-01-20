from django.db import models

class Appointments(models.Model):
    doctorName = models.CharField(max_length=20)
    patientName = models.CharField(max_length=20)
    doctorPrice = models.IntegerField(default=100)
    appointmentDate = models.DateField()
    payment_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.id