from django.db import models
from datetime import datetime


class Question(models.Model):

    title = models.CharField('Question', help_text="Max 200 characters", max_length=200)

    author = models.CharField('Your name', max_length=50)

    pub_date = models.DateTimeField('date published', default=datetime.now)
