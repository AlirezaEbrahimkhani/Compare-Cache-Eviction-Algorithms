FROM python:3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR server

CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000
