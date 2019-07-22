# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:latest
RUN apt-get update
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /app

# Set the working directory to /music_service
WORKDIR /app

# Copy the current directory contents into the container at /music_service
ADD . /app/
RUN curl https://bootstrap.pypa.io/get-pip.py | python
# Install any needed packages specified in requirements.txt
RUN  pip install -r requirement.txt
RUN  pip install git+https://github.com/django-extensions/django-extensions.git@master
# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000
# CMD specifcies the command to execute to start the server running.
ENTRYPOINT ["/bin/bash", "-c", "python manage.py runserver"]
# done!

