from django.urls import path
from todoAuth.views import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    # path('logout/', LogoutView.as_view(), name='auth_logout'),
]