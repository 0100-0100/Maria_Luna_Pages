from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField('get_icon_url')

    class Meta:
        model = Location
        fields = (
            'id', 'name', 'description', 'phone', 'instagram_link',
            'facebook_link', 'website_link', 'email', 'x', 'y', 'icon_url'
        )

    def get_icon_url(self, location):
        request = self.context.get('request')
        if location.icon is not None:
            icon_url = location.icon.image.url
            return request.build_absolute_uri(icon_url)
        return None
