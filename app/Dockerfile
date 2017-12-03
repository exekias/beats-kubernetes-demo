FROM python:3.6.3

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /src
ENV DJANGO_SETTINGS_MODULE=app.settings

RUN mkdir -p /src/app
WORKDIR /src/app
ADD requirements.txt /src/app/
RUN pip install -r requirements.txt
ADD . /src/app/

CMD ["uwsgi", "--socket", ":8081", "-T", "--wsgi-file", "wsgi.py"]
