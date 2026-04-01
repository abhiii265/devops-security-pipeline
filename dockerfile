FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy everything from your current local folder into the /app folder
COPY . /app

# Install the Python dependencies
RUN pip install -r requirements.txt

# Start the Django server when the container runs
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
