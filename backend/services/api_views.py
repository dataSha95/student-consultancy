from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer

class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.all().order_by('-created_at')
    serializer_class = ServiceSerializer
