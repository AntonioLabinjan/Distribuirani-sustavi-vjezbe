FROM python:3.12-slim

WORKDIR /app

COPY . .

# Instaliramo potrebne pakete s zaključanim verzijama
RUN pip install --no-cache-dir \
    fastapi==0.111.1 \
    uvicorn[standard]==0.24.0 \
    requests==2.32.0 \
    jinja2==3.1.6 \
    python-multipart==0.0.9 

EXPOSE 5000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
