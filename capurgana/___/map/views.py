"""Map views module."""
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListAPIView
from .models import Location
from .serializers import LocationSerializer
from django.http import JsonResponse
import json


class LocationListView(ListAPIView):
    """LocationListView class API view."""

    queryset = Location.objects.all()
    serializer_class = LocationSerializer


@login_required
def bulk_update_locations(request):
    """Post endpoint API view for receiving location updates."""
    if request.method == 'POST':
        if not request.user.is_staff:  # Only admin users allowed
            return JsonResponse(
                {'status': 'error', 'message': 'Permission denied'}, status=403
            )

        try:
            data = json.loads(request.body)
            updates = data.get('locations', [])
            for loc_data in updates:
                location = Location.objects.get(pk=loc_data['id'])
                location.x = loc_data['x']
                location.y = loc_data['y']
                location.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse(
                {'status': 'error', 'message': str(e)}, status=400
            )

    return JsonResponse(
        {'status': 'error', 'message': 'Invalid request'},
        status=400
    )
