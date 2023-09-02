FROM python:latest

RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

CMD python main.py