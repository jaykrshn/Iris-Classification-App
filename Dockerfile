# Use the official Python image as a base image
FROM python:3.9.19

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the working directory
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code to the working directory
COPY ./app/ /app/

# Expose a default port
EXPOSE 8000

# Run the application with Uvicorn, binding it to 0.0.0.0 so it can be accessed externally
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
