from django.db import models

# Create your models here.


class Hospitals(models.Model):
    hospital_id = models.CharField(max_length=20)
    hospital_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    class Meta:
        db_table = "HOSPITALS"


class Patient(models.Model):
    patient_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    permanent_address = models.CharField(max_length=20)
    current_address = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    hospital_id = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
     

    class Meta:
        db_table = "PATIENT"