from django.urls import path
from chat_room.views import *

urlpatterns = [
    path('room/', RoomView.as_view()),
    path('dialog/', Dialog.as_view())

]
