FROM python:3.8-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y awscli gcc g++ libglib2.0-0 libsm6 libxrender1 libxext6

# Set working directory
WORKDIR /app

# Copy the requirements file first (better caching)
COPY requirements.txt ./

# Install dependencies from requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Now copy the rest of the code
COPY . .

# Optional: Ensure correct versions of transformers and accelerate
RUN pip install --upgrade accelerate transformers

# Final command
CMD ["python3", "app.py"]
