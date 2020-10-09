#!/usr/bin/python3
# vim: set fileencoding=utf-8 ;


from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import devicesettings
from .serializers import devicesettingsSerializer



class devicesettingsViewSet(viewsets.ModelViewSet):
    queryset = devicesettings.objects

    def get_serializer_class(self):
        return devicesettingsSerializer
