from django.db import models
from datetime import datetime


class Question(models.Model):

    title = models.CharField('Question', help_text='Max 200 characters', max_length=200)

    author = models.CharField('Your name', max_length=50)

    pub_date = models.DateTimeField('date published', default=datetime.now)


class QuestionVote(models.Model):

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='votes')

    # We don't do strong checks on votes, just keep session id
    session_key = models.CharField(max_length=40)

    class Meta:
        unique_together = (('question', 'session_key'),)