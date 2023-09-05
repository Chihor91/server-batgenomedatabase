FROM python:3.11.4

ENV PYTHONBUFFERED 1

RUN mkdir /api

WORKDIR /api

ADD . /api/

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000