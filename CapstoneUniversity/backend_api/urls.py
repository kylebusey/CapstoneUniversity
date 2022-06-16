from django.urls import path
from .views import ObtainTokenPairView, UserCreateView, FacultyCreateView, UserTypeView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('students/register/', UserCreateView.as_view(), name="create_user"),
    path('faculty/register/', FacultyCreateView.as_view(), name="create_faculty_user"),
    path('token/obtain/', ObtainTokenPairView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('usergroup/', UserTypeView.as_view(), name="retrieve_user_group")
]