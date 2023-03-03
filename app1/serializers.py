from rest_framework import serializers
from .models import Dose

class DoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dose
        fields = ('dose_id', 'dose', 'patient_id', 'patient_name', 'machine_id')
