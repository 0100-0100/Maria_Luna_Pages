"""Core models module."""
from django.db import models


class Illustration(models.Model):
    """Illustration assets model."""

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='illustrations/')
    added = models.DateField(auto_now_add=True)

    def __str__(self):
        """__str__ dunder method."""
        return f"{self.name} | {self.added}"


class Photo(models.Model):
    """Photo assets model."""

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(null=True)
    added = models.DateField(auto_now_add=True)

    def __str__(self):
        """__str__ dunder method."""
        return f"{self.name} | {self.added}"


class Carousel(models.Model):
    """Model for relating Photos and Carousels."""

    name = models.CharField(max_length=255)
    show_description = models.BooleanField(default=False)
    images = models.ManyToManyField(
        Photo, related_name="carousels", blank=True
    )

    def get_description_and_image_urls(self):
        """Return a list of all images for a related carousel."""
        img_urls_list = []
        for _ in self.images.all():
            img_urls_list.append(
                {'url': _.image.url, 'description': _.description}
            )
        return img_urls_list

    def __str__(self):
        """__str__ dunder method."""
        return f"{self.name}"


class ShouldKnowSection(models.Model):
    """Model representing the sections for the what you should know about view."""

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text_content = models.TextField(null=True, default=None)
    button_text = models.CharField(max_length=255, null=True, default=None)
    button_link = models.CharField(max_length=500, null=True, default="#")
    image = models.ForeignKey(
        Photo, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='should_know_sections'
    )
    illustration = models.ForeignKey(
        Illustration,
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='should_know_sections'
    )
    added = models.DateField(auto_now_add=True)

    def __str__(self):
        """__str__ dunder method."""
        return f"{self.name}"
