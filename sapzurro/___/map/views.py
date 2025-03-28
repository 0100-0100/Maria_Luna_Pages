from rest_framework.generics import ListAPIView
from .models import Location
from .serializers import LocationSerializer

class LocationListView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
