from rest_framework import generics
from .models import Dose
from .serializers import DoseSerializer

class LastDoseView(generics.RetrieveAPIView):
    serializer_class = DoseSerializer
    lookup_field = 'machine_id'
    
    def get_queryset(self):
        machine_id = self.kwargs['machine_id']
        latest_dose = Dose.objects.filter(patient__machine__machine_id=machine_id).latest('dose_id')
        return [latest_dose]
