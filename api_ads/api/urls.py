from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import AdsListCreateView, AdRetrieveView


# url paths for api
urlpatterns = [
    path('v1/ads/', AdsListCreateView.as_view(), name='ads-list-create-view'),
    path('v1/ads/<int:pk>/', AdRetrieveView.as_view(), name='ads-get-by-id-view'),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
