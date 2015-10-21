from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.CharField(max_length=500)
    date_published = models.DateTimeField(auto_now_add=True)
    mes_user = models.ForeignKey(User)
    def __unicode__(self):
        return self.text