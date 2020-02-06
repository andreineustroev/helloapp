FROM python:3.8.1-slim-buster

RUN useradd helloapp
WORKDIR /home/helloapp

COPY requirements.txt /home/helloapp
COPY hello.py /home/helloapp

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

RUN chown -R helloapp:helloapp ./
USER helloapp
ENV FLASK_APP hello.py

EXPOSE 5000
ENTRYPOINT exec gunicorn -b :5000 --access-logfile - --error-logfile - hello:app