from rest_framework import routers
from django.conf.urls import url
from apps.gaming.views import PlatformViewSet, ReviewViewSet, GameViewSet,OneGameViewSet, DeveloperViewset

router = routers.DefaultRouter()
router.register('reviews', ReviewViewSet, basename='reviews')

custom_urlpatterns = [
    url(r'platforms/(?P<pk>\d+)/games$', PlatformViewSet.as_view(), name='platform_games'),
    url('developers/', DeveloperViewset.as_view(), name='developers'),
    url(r'games/(?P<pk>\d+)/$', OneGameViewSet.as_view(), name='single_game'),
    url('games/', GameViewSet.as_view(), name="games"),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
