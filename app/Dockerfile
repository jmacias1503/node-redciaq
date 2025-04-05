FROM python:3.13.2-alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python3", "main.py"]
