from django.contrib import admin
from django.urls import path
from rest_framework import routers

from services.views import SubsciptionView

urlpatterns = [
    path('admin/', admin.site.urls),
]


router = routers.DefaultRouter()
router.register(r'api/subsciptions', SubsciptionView)

urlpatterns += router.urls