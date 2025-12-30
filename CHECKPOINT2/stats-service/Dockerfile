FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi==0.111.1 uvicorn==0.24.0 requests==2.32.0 python-jose[cryptography]==3.3.0 python-multipart==0.0.9

EXPOSE 8001

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
