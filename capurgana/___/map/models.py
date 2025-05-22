"""Map Models module."""
from django.db import models

location_field_base_settings = {
    'null': True, 'blank': True, 'default': None, 'max_length': 255
}


class MapLogoIcon(models.Model):
    """Icon model."""

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='map_logos/')
    added = models.DateField(auto_now_add=True)

    def __str__(self):
        """__str__ dunder method."""
        return f"{self.name} | {self.added}"


class Location(models.Model):
    """Location | Represents a marker location on the map."""

    name = models.CharField(
        **location_field_base_settings,
        help_text="Name of the Location."
    )
    description = models.TextField(
        **location_field_base_settings,
        help_text="Long description of the Location."
    )
    phone = models.CharField(
        **location_field_base_settings,
        help_text="Phone number for the Location."
    )
    instagram_link = models.CharField(
        **location_field_base_settings,
        help_text="Link for Instagram if available."
    )
    facebook_link = models.CharField(
        **location_field_base_settings,
        help_text="Link for Facebook if available."
    )
    website_link = models.CharField(
        **location_field_base_settings,
        help_text="Link for a website if available."
    )
    email = models.CharField(
        **location_field_base_settings,
        help_text="Email for the Location."
    )
    x = models.FloatField(
        null=True, help_text="X-coordinate in pixels.", default=0
    )
    y = models.FloatField(
        null=True, help_text="Y-coordinate in pixels.", default=0
    )
    icon = models.OneToOneField(
        MapLogoIcon,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        related_name="map_location_marker",
        help_text="Icon for the location."
    )

    def __str__(self):
        """__str__ dunder method."""
        return self.name
