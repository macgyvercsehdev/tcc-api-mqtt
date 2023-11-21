FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app

WORKDIR /app

RUN pip install -U pip setuptools

ADD . /app

RUN mv /app/kubernetes/pip/.netrc /root/.netrc && mkdir -p /root/.pip && mv /app/kubernetes/pip/.pip/pip.conf /root/.pip/pip.conf && rm -r /app/kubernetes

RUN pip install -r /app/requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--port", "80", "--reload", "--host", "0.0.0.0"]
