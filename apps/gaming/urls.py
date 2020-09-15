from rest_framework import routers
from django.conf.urls import url
from apps.gaming.views import PlatformViewSet

router = routers.DefaultRouter()
# router.register('platforms', PlatformViewSet, basename='platforms')

custom_urlpatterns = [
    url(r'platforms/(?P<pk>\d+)/games$', PlatformViewSet.as_view(), name='platform_games')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns