from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Course, UserType
from .serializers import CourseSerializer, MyTokenObtainPairSerializer, \
    CourseDetailSerializer, UserSerializer, UserTypeSerializer


User = get_user_model()

class CourseView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserCreateView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            newUser = serializer.save()
            user_type = UserType(user=newUser, is_student=True)
            user_type.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacultyCreateView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            newUser = serializer.save()
            user_type = UserType(user=newUser, is_faculty=True)
            user_type.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTypeView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = UserTypeSerializer

    def get(self, request):
        userID = request.user.id
        userType = UserType.objects.get(user_id=userID)
        serializer = UserTypeSerializer(userType)
        if userType:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
