# Set the base image
FROM python:3.12.3

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Set the port
EXPOSE 8000

# Set the entrypoint command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]