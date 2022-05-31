FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements/txt

COPY ./Drum_Machine_Pygame ./drumapp

CMD ["python", "./Drum_Machine_Pygame/main.py"]

