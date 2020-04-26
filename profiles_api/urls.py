from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import UserProfileViewSet, UserLoginAPIView, UserProfileFeedViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('feed', UserProfileFeedViewSet)

urlpatterns= [
    path('login/', UserLoginAPIView.as_view()),
    path('',include(router.urls))
]