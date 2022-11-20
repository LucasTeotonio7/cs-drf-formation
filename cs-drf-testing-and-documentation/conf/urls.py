from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from aluraflix.views import ProgramViewSet

router = routers.DefaultRouter()
router.register('programs', ProgramViewSet, basename='programs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
