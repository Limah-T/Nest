FROM python:3.13-slim

# Create the directory in the container as /app if it doesn't exist
WORKDIR /app 

# Copy dependency file first (improves cache usage) to the directory => /app/requirements.txt
COPY requirements.txt .         
RUN pip install --no-cache-dir -r requirements.txt

# Everything from build context → /app except the ones in the dockerignore
COPY . .

# RUN the command below
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
