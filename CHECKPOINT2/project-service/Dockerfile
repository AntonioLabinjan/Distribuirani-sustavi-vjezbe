FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi==0.111.1 uvicorn==0.24.0 pydantic==1.10.12 python-jose[cryptography]==3.3.0  PyJWT==2.8.0

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]