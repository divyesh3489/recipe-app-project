# This is the base image for the Docker container. It is a lightweight version of Python 3.9 that is based on Alpine Linux 3.13.
FROM python:3.9-alpine3.13  

# This is the metadata for the image. It specifies the maintainer of the image.
LABEL maintainer="divyesh"

# This environment variable ensures that Python output is sent straight to the terminal without buffering it first.
ENV PYTHONUNBUFFERED 1 

# Copy the requirements.txt file from the local directory to the /tmp/ directory in the Docker container.
COPY ./requirements.txt /tmp/requirements.txt 

# Copy the app directory from the local directory to the /app/ directory in the Docker container. 
COPY ./app /app 

# Set the working directory to /app/ in the Docker container.
WORKDIR /app 

# Expose port 8000 to the outside world.
EXPOSE 8000
# Create a virtual environment in the /py/ directory.  Update pip to the latest version. Install the dependencies listed in the requirements.txt file. Remove the requirements.txt file. 
# Create a new user The user will not have a password. This flag prevents the creation of a home directory for the user..
# Install the PostgreSQL client library and the PostgreSQL development headers. This is required to install the psycopg2 package.
# This command installs the PostgreSQL development headers and the musl-dev package, which is required to build the psycopg2 package.
# Install the PostgreSQL development headers and the musl-dev package..
# Remove the PostgreSQL development headers and the musl-dev package. This reduces the size of the Docker image.
RUN python -m venv /py && \ 
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-dev \ 
        build-base postgresql-dev musl-dev && \ 
    /py/bin/pip install -r /tmp/requirements.txt && \ 
    rm -rf /tmp && \
    apk del .tmp-build-dev && \ 
    adduser \   
        --disabled-password \ 
        --no-create-home \
        django-user

# Add the /py/bin directory to the PATH environment variable. This ensures that the virtual environment is used when running Python commands.
ENV PATH="/py/bin:$PATH" 

# Switch to the django-user user.
USER django-user


