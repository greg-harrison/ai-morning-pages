# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 5002

# Define environment variable
ENV NAME Test
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5002

# Run app.py when the container launches
CMD ["python", "app.py"]