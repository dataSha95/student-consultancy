from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all().order_by('-event_date')
    serializer_class = EventSerializer
