FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
    awscli \
    gcc \
    g++ \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libprotobuf-dev \
    git \
    curl \
    && apt-get clean

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
