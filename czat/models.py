from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    """Klasa reprezentująca wiadomość w systemie"""
    text = models.CharField('message content', max_length=250)
    data_pub = models.DateTimeField('date of publication', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

