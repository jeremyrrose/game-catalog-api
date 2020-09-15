from rest_framework import routers
from django.conf.urls import url
from apps.gaming.views import PlatformViewSet, ReviewViewSet, GameViewSet

router = routers.DefaultRouter()
router.register('reviews', ReviewViewSet, basename='reviews')

custom_urlpatterns = [
    url(r'platforms/(?P<pk>\d+)/games$', PlatformViewSet.as_view(), name='platform_games'),
    url(r'games/(?P<pk>\d+)/$', GameViewSet.as_view(), name='games'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
