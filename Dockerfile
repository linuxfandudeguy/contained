# Use an official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install required packages
RUN pip install requests html2text

# Copy the script that fetches HTML into the container
COPY index.py .

# Set the entrypoint to handle arguments
ENTRYPOINT ["python", "index.py"]
