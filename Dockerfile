# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y python3-pip

# Set the working directory to /app
WORKDIR /safa_backend

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /safa_backend

# Set the host to your IPv4 address
ENV HOST=192.168.1.139

# Expose the port that your Django app will be running on
EXPOSE 8000

# Start the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
