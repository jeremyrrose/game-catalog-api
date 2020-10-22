from rest_framework import status, viewsets  # this helps us to know HTTP status of our request
from rest_framework.response import Response  # We need this to convert DB query to JSON
from rest_framework.views import APIView
# Not all the models need CRUD, sometimes all we need to do is read
from rest_framework.viewsets import ReadOnlyModelViewSet
# we can allow all the users to see the view
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import RegistrationSerializer, LoginSerializer,  UserInfoSerializer, UserListSerializer
from .models import User
from apps.gaming.models import Review
from rest_framework import generics


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "email": request.data.get('email'),
                "username": request.data.get('username'),
                "password": request.data.get('password'),
                "first_name": request.data.get('first_name'),
                "last_name": request.data.get('last_name'),
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserListViewSet(ReadOnlyModelViewSet):
    """
    This view set automatically provides `list` and `detail` actions.
    """

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserListSerializer


class OneUser(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserInfoSerializer

    def get_queryset(self):
        if self.kwargs.get('pk'):
            user = User.objects.filter(pk=self.kwargs['pk'])
            queryset = user
            return queryset

    def partial_update(self, request, *args, **kwargs):
        if self.kwargs.get('pk'):
            users = User.objects.filter(pk=self.kwargs['pk'])
            user = User.objects.get(pk=self.kwargs['pk'])
            user.watch_list.clear()
            user.watch_list.set(request.data.get('watch_list', user.watch_list))
            user.save()

            serializer = UserInfoSerializer(user)
            return Response(serializer.data)

class OneUser(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserInfoSerializer

    def get_queryset(self):
        if self.kwargs.get('pk'):
            user = User.objects.filter(pk=self.kwargs['pk'])
            queryset = user
            return queryset

    def partial_update(self, request, *args, **kwargs):
        if self.kwargs.get('pk'):
            users = User.objects.filter(pk=self.kwargs['pk'])
            user = User.objects.get(pk=self.kwargs['pk'])
            if user == self.request.user:
                user.watch_list.clear()
                user.watch_list.set(request.data.get('watch_list', user.watch_list))
                user.save()

            serializer = UserInfoSerializer(user)
            return Response(serializer.data)
