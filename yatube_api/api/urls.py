from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)

from .views import PostViewSet, GroupViewSet, FollowViewSet

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='post')
router_v1.register(r'groups', GroupViewSet, basename='group')
router_v1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/posts/<int:post_id>/comments/',
         include('api.comments_urls')),
    path('v1/jwt/create/', TokenObtainPairView.as_view(),
         name='jwt_create'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(),
         name='jwt_refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]
