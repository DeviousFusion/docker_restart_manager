# docker_restart_manager
This project allows you to automatically restart Docker containers based on schedules specified through container labels.

## Usage
```
version: '3.8'

services:
  my_service:
    image: my-container-image
    labels:
      - "drm.restart.schedule=03:00,15:00"
    # Other configuration like ports, volumes, etc.

  restart_cron:
    build: .
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock # This is important to allow the container to control the host docker instance
```
