FROM python:3.12-slim

WORKDIR /app

COPY . .

# instaliraj sve potrebne pakete
RUN pip install fastapi uvicorn requests jinja2 python-multipart

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
