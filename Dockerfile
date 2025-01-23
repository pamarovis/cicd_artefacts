# Aprašome koks naudojamas image
FROM python:latest

# Nustatome working directory
WORKDIR /app

# nukopijuojame failą
COPY app.py .

# Paleidžiame programą
CMD ["python", "app.py"]
