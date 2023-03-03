
from django.db import models
import uuid

class Machine(models.Model):
    machine_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    machine_name = models.CharField(max_length=255)

class Patient(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='patients')
    patient_name = models.CharField(max_length=255)

class Dose(models.Model):
    dose_id = models.AutoField(primary_key=True)
    dose = models.FloatField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doses')
