FROM python:3.8-slim-buster


WORKDIR /code
RUN apt-get update && apt-get install -y pkg-config




COPY requirement.txt requirement.txt

RUN pip install -r requirement.txt

COPY . .

EXPOSE 8000
CMD python manage.py runserver