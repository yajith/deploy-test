# Use a Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Run the application
CMD ["python", "client.py"]

