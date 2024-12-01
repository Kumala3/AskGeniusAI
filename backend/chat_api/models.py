from django.db import models
from django.contrib.auth.models import User


class HistoricalFigure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    era = models.CharField(max_length=100)
    prompt_template = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ChatSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    historical_figure = models.ForeignKey(HistoricalFigure, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ChatMessage(models.Model):
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    content = models.TextField()
    is_user = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
