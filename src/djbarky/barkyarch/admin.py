from django.contrib import admin
from .models import Patient, HealthMetric, TreatmentPlan

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'medical_history')
    search_fields = ('name',)

class HealthMetricAdmin(admin.ModelAdmin):
    list_display = ('patient', 'type', 'value', 'recorded_at')
    list_filter = ('type',)
    date_hierarchy = 'recorded_at'

class TreatmentPlanAdmin(admin.ModelAdmin):
    list_display = ('patient', 'description', 'start_date', 'end_date')
    list_filter = ('start_date',)

admin.site.register(Patient, PatientAdmin)
admin.site.register(HealthMetric, HealthMetricAdmin)
admin.site.register(TreatmentPlan, TreatmentPlanAdmin)
