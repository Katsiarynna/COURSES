from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from . import consumers, views
from .endpoints import (
    ConversationRequestViewSet,
    MessageAPIView,
    MessageViewSet,
    RoomViewSet,
)

router = DefaultRouter()
router.register("room", RoomViewSet)
router.register("request", ConversationRequestViewSet)
router.register("message", MessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("message/", MessageAPIView.as_view(), name="message"),
    path("", views.index_view, name="chat-index"),
    path("<str:room_name>/", views.room_view, name="chat-room"),
]


websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
