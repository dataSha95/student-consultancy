from rest_framework import generics
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated


class ApplicationCreateAPIView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationListAPIView(generics.ListAPIView):
    queryset = Application.objects.all().order_by('-submitted_at')
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

