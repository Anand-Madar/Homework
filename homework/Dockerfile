# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install the required packages directly
RUN pip install pandas sqlalchemy psycopg2-binary pyarrow

# Copy your python script into the container
# (Change 'pipeline.py' if your script is named something else)
COPY dataset.py .

# Run the script when the container launches
ENTRYPOINT ["python", "dataset.py"]