from django.db import models
from datetime import datetime


class Message(models.Model):

    message = models.CharField(max_length=140)

    author = models.CharField(max_length=50)

    pub_date = models.DateTimeField('date published', default=datetime.now)
