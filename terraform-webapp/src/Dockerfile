FROM python:3.8-buster

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY weather.py .

EXPOSE 8080

CMD ["python", "weather.py"]
