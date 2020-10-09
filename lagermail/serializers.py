from rest_framework import serializers
from .models import devicesettings


class devicesettingsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = devicesettings
        fields = "__all__"
