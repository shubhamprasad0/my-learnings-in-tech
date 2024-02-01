# This is a sample Dockerfile
FROM node:21-alpine

# Ideally, don't set env var in the image and configure it externally
# especially when the env can change for the application
# So that, if the env changes, we do not have to build the image again
ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PASSWORD=password

# execute any linux command inside the container
RUN mkdir -p /home/app

# copy contents from host machine to the container image
COPY . /home/app

# Define the entrypoint which `docker run <image>` will run
# Can have multiple RUN commands, but CMD is just one and defines the entrypoint command
CMD ["node", "/home/app/server.js"]