from django.urls import include, path
from rest_framework import routers
from .views import PatientViewSet, HealthMetricViewSet, UserViewSet  # Import your actual viewsets

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'healthmetrics', HealthMetricViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),  # Prefixed with 'api/' for clarity
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # For browsable API authentication
]
