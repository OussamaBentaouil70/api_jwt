# Use the official Python base image
FROM python:3.12.3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port that the Django application will run on
EXPOSE 8000

# Set the command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]