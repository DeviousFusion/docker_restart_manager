FROM python:3.12-slim

# Copy the script into the container
COPY main.py /usr/src/app/main.py

# Install docker package
RUN pip install docker

# Set the working directory
WORKDIR /usr/src/app

# Run the script
CMD [ "python", "./main.py" ]