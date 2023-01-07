FROM python:3.9.0

ENV PYTHONUNBUFFERED l
#ENV DJANGO_ENV dev

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . /app/

#RUN echo "SECRET_KEY=django-insecure-$ioa*(%5%p#1&c(as*.._&d+x-+(-pdyo&z+" > .env
#EXPOSE 8000

# default run, can be overridden in docker compose.
#CMD gunicorn demoproject.wsgi:application --bind 0.0.0.0:8000 --workers 3