from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import *
from django.urls import path


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', UserRegister.as_view(), name='signup'),
    
    
  
]