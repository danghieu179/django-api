from django.conf.urls import include, url
from .views import CustomerViewSet, ManufacturerSerializerViewSet

urlpatterns = [
    url(r'', include(api_router.urls))
]
