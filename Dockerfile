FROM python:3.9.0

WORKDIR /home/

RUN echo "test_myvenue"

RUN git clone https://github.com/bonofaber/Django_pybo_Goodvenue

WORKDIR /home/Django_pybo_Goodvenue

RUN pip install -r requirements.txt


RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
