#!/usr/bin/python3
# vim: set fileencoding=utf-8 ;


from rest_framework.routers import DefaultRouter

from lagermail.views import devicesettingsViewSet


router = DefaultRouter()
router.register(r"lagermail", devicesettingsViewSet)
