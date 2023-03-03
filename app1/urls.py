from django.urls import path
from .views import LastDoseView

urlpatterns = [
    path('api/<uuid:machine_id>/', LastDoseView.as_view(), name='last_dose'),
]
