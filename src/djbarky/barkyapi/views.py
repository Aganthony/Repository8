from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Patient, HealthMetric, TreatmentPlan
from .permissions import IsPatientOrHealthcareProviderOrReadOnly  # Adjusted permission class
from .serializers import PatientSerializer, HealthMetricSerializer, TreatmentPlanSerializer, UserSerializer

# Patient viewset
class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsPatientOrHealthcareProviderOrReadOnly]

# HealthMetric viewset
class HealthMetricViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for health metrics.
    """
    queryset = HealthMetric.objects.all().order_by('-recorded_at')
    serializer_class = HealthMetricSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsPatientOrHealthcareProviderOrReadOnly]

# TreatmentPlan viewset
class TreatmentPlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows treatment plans to be viewed or edited.
    """
    queryset = TreatmentPlan.objects.all()
    serializer_class = TreatmentPlanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsPatientOrHealthcareProviderOrReadOnly]

# User viewset
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
