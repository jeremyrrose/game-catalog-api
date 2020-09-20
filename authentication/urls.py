from django.conf.urls import url
from authentication.views import RegistrationAPIView, LoginAPIView, UserListViewSet, OneUser
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'many', OneUser, basename='user')


urlpatterns = [
    url(r'^users/$', UserListViewSet.as_view({'get': 'list'}), name='user_list'),
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginAPIView.as_view(), name='login'),
]

urlpatterns += router.urls