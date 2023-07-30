FROM python:3.8.0-slim-buster


WORKDIR /app

COPY . /artifacts 
COPY . /app

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]