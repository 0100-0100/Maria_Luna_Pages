from django.db import models


class MapLogoIcon(models.Model):
    """Icon model."""
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='map_logos/')
    added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.added}"

class Location(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the Location.", default=None)
    phone = models.CharField(null=True, blank=True, default=None, max_length=255, help_text="Phone number for the Location.")
    description = models.TextField(null=True, blank=True, default=None, help_text="Long description of the Location.")
    email = models.CharField(null=True, blank=True, default=None, max_length=255, help_text="Email for the Location.")
    instagram_link = models.CharField(null=True, blank=True, default=None, max_length=255, help_text="Link for Instagram if available.")
    website_link = models.CharField(null=True, blank=True, default=None, max_length=255, help_text="Link for a website if available.")
    x = models.FloatField(null=True, help_text="X-coordinate in pixels.", default=0)
    y = models.FloatField(null=True, help_text="Y-coordinate in pixels.", default=0)
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
        return self.name
