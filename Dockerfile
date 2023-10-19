# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy Scores.txt to /Scores.txt in the container
COPY Scores.txt /Scores.txt

EXPOSE 5000

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN mkdir -p /app/Scores
# Command to run the Flask application
CMD ["python3", "Main_Game.py"]