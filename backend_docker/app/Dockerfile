# Use the official Python image as the base image
FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
  && pip install --upgrade pip

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents of the application to /stateCompany in the container
COPY . /app/


# Define the command to run when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]