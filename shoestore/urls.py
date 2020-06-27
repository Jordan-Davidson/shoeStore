from django.urls import path, include
from rest_framework import routers

from api import views as api_views

router = routers.DefaultRouter()
router.register(r'manufacturer', api_views.ManufacturerViewset)
router.register(r'shoecolor', api_views.ShoeColorViewSet)
router.register(r'shoetype', api_views.ShoeTypeViewSet)
router.register(r'shoe', api_views.ShoeViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
