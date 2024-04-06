FROM python:3.12.1-slim-bullseye

WORKDIR /app

ENV PYTHONPATH=.
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "main.py" ]