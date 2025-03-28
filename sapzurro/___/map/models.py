from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    x = models.IntegerField(help_text="X-coordinate in pixels")
    y = models.IntegerField(help_text="Y-coordinate in pixels")
    icon = models.ImageField(upload_to='icons/', help_text="Icon for the location")

    def __str__(self):
        return self.name
