from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    invited = models.ManyToManyField(User, verbose_name="Участники", related_name="invited_user")
    date = models.DateTimeField("Дата создания", auto_now=True)

    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комната чата"


class Chat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Комната чата")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    text = models.TextField("Сообщение", max_length=250)
    date = models.DateTimeField("Дата отправки", auto_now=True)

    class Meta:
        verbose_name = "Сообщения чата"
        verbose_name_plural = "Сообщение чата"
