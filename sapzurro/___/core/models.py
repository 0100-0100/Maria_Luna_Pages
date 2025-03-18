from django.db import models

class Photo(models.Model):
    """Photo assets model."""
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(null=True)
    added = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} | {self.added}"

class Carousel(models.Model):
    """Model for relating Photos and Carousels."""
    name = models.CharField(max_length=255)
    show_description = models.BooleanField(default=False)
    images = models.ManyToManyField(Photo, related_name="carousels", blank=True)

    def get_image_urls(self):
        img_urls_list = []
        for _ in self.images.all():
            img_urls_list.append({'url': _.image.url})
        return img_urls_list

    def __str__(self):
        return f"{self.name}"
