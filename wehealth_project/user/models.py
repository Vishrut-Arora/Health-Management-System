from django.db import models


class User(models.Model):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    is_pharmacy = models.BooleanField(default=False)
    is_insurance_firm = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)
    type_auth = models.IntegerField()
    role_proof_image = models.ImageField()
    auth_id = models.IntegerField()
    auth_image = models.ImageField()
    email = models.EmailField()
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=32)
    is_authorized = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=False)
    is_login = models.BooleanField(default=False)

    def __str__(self):
        return str(self.auth_id)
