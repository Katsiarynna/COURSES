from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .endpoints import \
      (RoomViewSet, ConversationRequestViewSet, MessageViewSet, MessageAPIView)
from . import views

router = DefaultRouter()
router.register("room", RoomViewSet)
router.register("request", ConversationRequestViewSet)
router.register("message", MessageViewSet)

urlpatterns = [
      path("", include(router.urls)),
      path("message/", MessageAPIView.as_view(), name="message"),
      path('', views.index_view, name='chat-index'),
      path('<str:room_name>/', views.room_view, name='chat-room'),
]
