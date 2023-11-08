# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port that your FastAPI application will run on
EXPOSE 8000

# Define the command to run your FastAPI application
CMD ["python", "main.py"]
