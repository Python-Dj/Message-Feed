from django.db import models
from account.models import User




class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    title = models.CharField(max_length=25, null=True)
    content = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True, related_name="likes")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name="likes")
    crerated_at = models.DateTimeField(auto_now_add=True)
