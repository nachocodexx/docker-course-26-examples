# Bind volumes

In this exercise, we will learn how to bind volumes to a container. This allows us to share files between the host and the container.

1. Create a new directory on your host machine called "data":

```bash
mkdir data
```

2. Start a new container and bind the "data" directory to the container's "/data" directory:

```bash
docker run --name=container3 -v ./data:/data -ti ubuntu
```