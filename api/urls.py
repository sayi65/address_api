from django.conf.urls import url, include
from rest_framework  import routers
from .views import AddressViewSet

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)