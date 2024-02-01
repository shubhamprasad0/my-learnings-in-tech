# Docker

## Basics
- Image: the package with the application, configuration, and the environment (when not running)
- Container: the image when running; a running environment for the image.
- Can start multiple containers from the same image

## Docker Container vs Virtual Machine
- An operating system can be thought of as having two layers:-
  - Applications Layer
  - Kernel Layer
- A docker container virtualizes only the applications layer, and uses the kernel of the host
- A virtual machine virtualizes both the applications layer and the kernel.
- So, a virtual machine image of any OS can run on any host OS using a VM software (like VMWare).
- A docker container uses the kernel of the host OS. So, the images must be compatible. Then how do Linux based images work on Windows and MacOS. Because, Windows has WSL2 which is a full Linux kernel. And, Docker installs and runs a Linux VM on MacOS. This is how Linux based images work on Windows and MacOS too. Also, we can build multi platform images, through which docker will pick the appropriate image to start the container based on the architecture and the OS.

## Basic Docker Commands

- `docker pull <image>:<version>` -- pull image
- `docker images` -- list out available images on your machine
- `docker run <image>:<tag>` -- pull (if not available) and run an image and start a container from the image
- `docker run -d <image>:<tag>` -- run in detached mode, doesn't block the terminal and runs in the background. It returns the container id.
- `docker run --name <container_name> <image>:<tag>` -- specify name of container yourself instead of relying on the random name assignment
- `docker run -p <host_port>:<container_port> <image>:<tag>` -- specify port bindings; remember the host_port comes first. (Trick to remember: You think about yourself first, so specify your port first before thinking about the container's port)
- `docker ps` -- list running containers
- `docker ps -a` -- list all containers (running as well as not running)
- `docker stop <container_id or container_name>` -- stop a running container
- `docker start <container_id or container_name>` -- start a previously stopped container. Different from `docker run` as `docker run` creates a new container from an image. `docker start` starts an already created and previously stopped container. A stopped container remembers the config done during `docker run` (like the port bindings, etc.). So, `docker start` will use the same config.
- `docker logs <container_id or container_name>` -- check logs of the container by id or name
- `docker exec -ti <container_id or container_name> /bin/bash` -- To log in inside the container environment in interactive mode
- `docker --help` -- To get help on commands

## Docker Network
- Docker containers can communicate with each other using the container name if they are on the same network.
- `docker network ls` -- list existing docker networks
- `docker network create <network_name>` -- create new docker network

## Docker Compose
- used to manage a collection of containers which are used together in an application
- docker-compose will create a common network for the containers configured in the compose file
- Docs: https://docs.docker.com/compose/compose-file/

## Dockerfile
- Blueprint for creating docker images
- Docs: https://docs.docker.com/engine/reference/builder/

## Docker build
- `docker build -t <image_name>:<image_version> <path_of_Dockerfile>`

## Docker Volumes
- Persist data for containers; otherwise data gets lost when we stop the container
- Volume is a physical host file system location, which is mounted into the virtual file system of docker containers
- 3 Volume Types:-
  - **Host Volumes:-**
    - `docker run -v <host_path>:<container_path>` 
    - E.g. `docker run -v /home/mount/data:/var/lib/mysql/data`
    - You decide where on the host file system the reference is made
  - **Anonymous Volumes:-**
    - `docker run -v <container_path>`
    - E.g. `docker run -v /var/lib/mysql/data`
    - For each container, a directory is generated on the host by docker and automatically mounted
  - **Named Volumes:-**
    - `docker run -v <volume_name>:<container_path>`
    - E.g. `docker run -v mysqlvolume:/var/lib/mysql/data`
    - Similar to anonymous volumes as this is also created automatically by docker
    - Different as in we can specify a name for the volume, so it is no longer anonymous
    - We can reference the volume by name
    - Mostly used; should be used in production
- In Docker Compose:-
  ```yaml
  version: '3'
  services:
    mysql:
        image: mysql
        ...
        volumes:
            - db-data:/var/lib/mysql/data # same format as docker run commands above can be used; volume definition below
  volumes: # define all the volumes
    db-data
  ```