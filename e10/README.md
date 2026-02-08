# Connecting container: Network bridge

This project demonstrates how to configure container networking using Docker. It covers building a Python API image and running it using two different networking strategies: the **User-Defined Bridge** (recommended) and the **Default Bridge**.


## Prerequisites

- Docker installed on your machine.
- Basic understanding of terminal commands.

## Building image

1. Navigate to the project directory:
```bash
cd e9
```
2. Build the Docker image using the provided `Dockerfile`:
```bash
docker build -f ./Dockerfile -t test_api .
```
## Running container with Default Bridge
1. Run the container using the default bridge network:
```bash
    docker run --rm -d --name=c1 -p 9000:8000 test_api
    docker run --rm -d --name=c2 -p 9001:8000 test_api
```

2. Check ip address of the container:
```bash
    docker inspect c1 | grep IPAddress
    docker inspect c2 | grep IPAddress
```

3. Test connectivity between the containers using their IP addresses:
```bash
    docker exec c1 curl http://<IP_ADDRESS_OF_C2>:8000
    docker exec c2 curl http://<IP_ADDRESS_OF_C1>:8000
```
4. Test connectivity using domain names (this will fail because the default bridge does not support automatic DNS resolution):
```bash
    docker exec c1 curl http://c2:8000
    docker exec c2 curl http://c1:8000
```
## Running container with User-Defined Bridge
1. Create a user-defined bridge network:
```bash
    docker network create my-net
```
2. Run the containers and connect them to the user-defined bridge network:
```bash
    docker run --rm -d --name=c1 --network=my-net -p 9000:8000 test_api
    docker run --rm -d --name=c2 --network=my-net -p 9001:8000 test_api
```
3. Test connectivity using domain names (this will succeed because the user-defined bridge supports automatic DNS resolution):
```bash    docker exec c1 curl http://c2:8000
    docker exec c2 curl http://c1:8000
``` 
