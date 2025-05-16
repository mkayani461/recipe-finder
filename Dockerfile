# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy your app files into the container
COPY . .

# Install Flask and requests
RUN pip install flask requests

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

