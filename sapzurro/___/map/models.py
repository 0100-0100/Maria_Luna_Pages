from django.db import models
from core.models import Photo

class Location(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the Location.", default="Location Name")
    phone = models.CharField(null=True, max_length=255, help_text="Phone number for the Location.")
    description = models.TextField(null=True, help_text="Long description of the Location.")
    email = models.CharField(null=True, max_length=255, help_text="Email for the Location.")
    instagram_link = models.CharField(null=True, max_length=255, help_text="Link for Instagram if available.")
    website_link = models.CharField(null=True, max_length=255, help_text="Link for a website if available.")
    icon = models.ManyToManyField(Photo, blank=True, related_name="map_location_marker", help_text="Icon for the location.")
    x = models.IntegerField(null=True, help_text="X-coordinate in pixels.")
    y = models.IntegerField(null=True, help_text="Y-coordinate in pixels.")

    def __str__(self):
        return self.name
