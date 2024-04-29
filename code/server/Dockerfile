## Backend

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN mkdir -p opt/app/

WORKDIR /opt/app

# Copy the current directory contents into the container at /music_service
COPY ./code/server/ ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
