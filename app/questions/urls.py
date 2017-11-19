from django.conf.urls import url

from . import views


app_name = 'questions'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit/$', views.QuestionCreate.as_view(), name='create'),
    url(r'^vote/(?P<question_id>[0-9]+)$', views.vote, name='vote'),
]
