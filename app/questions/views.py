from django.shortcuts import render

from .models import Question


def index(request):
  questions = Question.objects.order_by('-pub_date')[:30]
  context = {'questions': questions}
  return render(request, 'questions/index.html', context)
