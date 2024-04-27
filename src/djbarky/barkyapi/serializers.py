from .models import Patient, HealthMetric, TreatmentPlan
from django.contrib.auth.models import User
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    health_metrics = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    treatment_plans = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ('id', 'name', 'date_of_birth', 'medical_history', 'health_metrics', 'treatment_plans')

class HealthMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetric
        fields = ('id', 'patient', 'type', 'value', 'recorded_at')

class TreatmentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentPlan
        fields = ('id', 'patient', 'description', 'start_date', 'end_date')

class UserSerializer(serializers.ModelSerializer):
    # Assuming that 'patients' is a reverse relation from User to Patient
    patients = serializers.PrimaryKeyRelatedField(many=True, queryset=Patient.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'patients']
