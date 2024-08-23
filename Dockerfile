FROM python:3.9

WORKDIR /app

COPY server/requirements.txt .
RUN pip install -r requirements.txt

COPY server /app

CMD ["python", "app.py"]