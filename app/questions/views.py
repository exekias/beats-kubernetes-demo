from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Question


def index(request):
  questions = Question.objects.order_by('-pub_date')[:30]
  context = {'questions': questions}
  return render(request, 'questions/index.html', context)

class QuestionCreate(CreateView):
    model = Question
    fields = ['title', 'author']
    success_url = reverse_lazy('questions:index')
