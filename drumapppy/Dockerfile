FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./drumapppy ./drumapp

CMD ["python", "./drumapppy/main.py"]
