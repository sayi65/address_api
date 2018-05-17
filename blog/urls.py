from rest_framework import routers
from .views import UserViewSet, EntryViewSet


blog_router = routers.DefaultRouter()
blog_router.register(r'users', UserViewSet)
blog_router.register(r'entries', EntryViewSet)