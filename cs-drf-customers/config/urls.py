from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.customer.views import CustomerViewSet

router = routers.DefaultRouter()
router.register('customers', CustomerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
