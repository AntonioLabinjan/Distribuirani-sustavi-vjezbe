# Koristimo službenu Python 3.12 slim sliku
FROM python:3.12-slim

# Postavimo working dir
WORKDIR /app

# Kopiramo sve fajlove u container
COPY . .

# Instaliramo potrebne pakete, uključujući multipart za form-data
RUN pip install --no-cache-dir \
    fastapi==0.111.1 \
    uvicorn[standard]==0.24.0 \
    "passlib[bcrypt]==1.7.4" \
    "bcrypt==4.0.1" \
    python-jose[cryptography]==3.3.0 \
    python-multipart==0.0.9 \
    requests==2.32.0 \
    PyJWT==2.8.0

# Expose porta
EXPOSE 8002

# Startamo uvicorn server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
