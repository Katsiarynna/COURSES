from django.contrib import admin

from .models import ConversationRequest, Message, Room

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(ConversationRequest)
