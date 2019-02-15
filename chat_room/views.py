from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from chat_room.models import *
from chat_room.serializers import *


class RoomView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})


class Dialog(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response({"status": "Access"})
        else:
            return Response({"status": "Error"})
