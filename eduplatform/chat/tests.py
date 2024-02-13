from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


from mentorship.consts import \
    (USER_DATA, create_user, create_room, create_message, create_conversationrequest)


from .serializers import (MessageSerializer, RoomSerializer, ConversationRequestSerializer)


__all__ = {"CreateRoomTest", 'ReadRoomTest', 'UpdateRoomTest', 'DeleteRoomTest',
           'CreateMessageTest', 'ReadMessageTest', 'UpdateMessageTest', 'DeleteMessageTest',
           'CreateConversationRequestTest', 'ReadConversationRequestTest',
           'UpdateConversationRequestTest', 'DeleteConversationRequestTest'}


class CreateRoomTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)

    def test_create_room(self):
        url = reverse("room-list")
        response = self.client.post(url, data={
            "user": self.user.id,
            "name": "Lucky"
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadRoomTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)
        self.room = create_room(self.user)

    def test_read_room_list(self):
        url = reverse("room-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_room_detail(self):
        url = reverse("room-detail", args=[self.room.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateRoomTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)
        self.room = create_room(self.user)
        self.data = RoomSerializer(self.room).data
        self.data.update({"name": "Bingo"})

    def test_update_room(self):
        url = reverse("room-detail", args=[self.room.id])
        response = self.client.put(url, self.data, format("json"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteRoomTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)
        self.room = create_room(self.user)

    def test_delete_room(self):
        url = reverse("room-detail", args=[self.room.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateMessageTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)
        self.room = create_room(self.user)

    def test_create_message(self):
        url = reverse("message-list")
        response = self.client.post(url, data={
            "user": self.user.id,
            "room": self.room.id,
            "content": "Very interesting"
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadMessageTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)
        self.room = create_room(self.user)
        self.message = create_message(self.user, self.room)

    def test_read_message_list(self):
        url = reverse("message-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_message_detail(self):
        url = reverse("message-detail", args=[self.message.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateMessageTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)
        self.room = create_room(self.user)
        self.message = create_message(self.user, self.room)
        self.data = MessageSerializer(self.message).data
        self.data.update({"content": "Not so interesting anymore"})

    def test_update_message(self):
        url = reverse("message-detail", args=[self.message.id])
        response = self.client.put(url, self.data, format("json"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteMessageTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)
        self.room = create_room(self.user)
        self.message = create_message(self.user, self.room)

    def test_delete_message(self):
        url = reverse("message-detail", args=[self.message.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateConversationRequestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)

    def test_create_conversationrequest(self):
        url = reverse("conversationrequest-list")
        response = self.client.post(url, data={
            "from_user": self.user.id,
            "to_user": self.user.id,
            "message": "Test for my chat"
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadConversationRequestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)
        self.room = create_room(self.user)
        self.message = create_message(self.user, self.room)
        self.conversationrequest = create_conversationrequest(user_id=self.user.id)  # Create a ConversationRequest object

    def test_read_conversationrequest_list(self):
        url = reverse("conversationrequest-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_conversationrequest_detail(self):
        url = reverse("conversationrequest-detail", args=[self.conversationrequest.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateConversationRequestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)
        self.room = create_room(self.user)
        self.message = create_message(self.user, self.room)
        self.conversationrequest = create_conversationrequest(user_id=self.user.id)
        self.data = ConversationRequestSerializer(self.conversationrequest).data
        self.data.update({"message": "Only test"})

    def test_update_conversationrequest(self):
        url = reverse("conversationrequest-detail", args=[self.conversationrequest.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteConversationRequestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.force_login(self.user)
        self.room = create_room(self.user)
        self.message = create_message(self.user, self.room)
        self.conversationrequest = create_conversationrequest(user_id=self.user.id)

    def test_delete_conversationrequest(self):
        url = reverse("conversationrequest-detail", args=[self.conversationrequest.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)








