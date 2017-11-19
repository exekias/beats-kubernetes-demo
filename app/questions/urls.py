from django.conf.urls import url

from . import views


app_name = 'questions'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit/$', views.QuestionCreate.as_view(), name='create'),
]
