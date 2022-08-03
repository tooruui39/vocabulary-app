from django.urls import include, path
from rest_framework import routers
from a1.views import VocabViewSet

routers = routers.DefaultRouter()
routers.register(r'', VocabViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
