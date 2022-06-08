FROM python:3.8-alpine

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "ats_scrap/main.py"]