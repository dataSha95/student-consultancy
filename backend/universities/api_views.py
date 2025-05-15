from rest_framework import generics
from .models import University
from .serializers import UniversitySerializer

class UniversityListAPIView(generics.ListAPIView):
    queryset = University.objects.all().order_by('-created_at')
    serializer_class = UniversitySerializer
