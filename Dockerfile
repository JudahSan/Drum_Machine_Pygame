FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

COPY ./drumapppy ./drumapp

CMD ["python", "./drumapppy/main.py"]

