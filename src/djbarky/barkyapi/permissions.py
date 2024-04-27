from rest_framework import permissions

class IsPatientOrHealthcareProviderOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow patients or their healthcare providers to edit patient data.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Determine if the request user is the patient
        is_patient = obj == request.user.patient_profile
        # Determine if the request user is the healthcare provider of the patient
        is_healthcare_provider = request.user in obj.healthcare_providers.all()

        # Write permissions are only allowed to the patient or their healthcare provider.
        return is_patient or is_healthcare_provider
