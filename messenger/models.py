from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)

def messages_changed(sender, **kwards):
    instance = kwards.pop('instance', None)
    action = kwards.pop('action', None)
    pk_set = kwards.pop('pk_set',None)
    print(instance, action , pk_set)

m2m_changed.connect(messages_changed, sender = Thread.messages.through)