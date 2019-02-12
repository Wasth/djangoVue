from rest_framework import serializers
from chat_room.models import *
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):
    creater = UserSerializers()
    invited = UserSerializers(many=True)

    class Meta:
        model = Room
        fields = ("creater", "invited", "date")


class ChatSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Chat
        fields = ("user", "text", "date")
