# Connecting container: Network bridge
In this scenario, we simulate a web container communicating with a db (database) container using alpine Linux images.

- 1. Create a network
First, create a logical network to host the containers.

```bash
docker network create my-net
```
- 2. Run the Database container
Run a container named db in the background. By giving it a specific name, Docker allows other containers on the same network to find it via DNS.

```bash
docker run -d --network my-net --name db alpine sleep 1000
```
- 3. Run the Web container
Run a second container named web on the same network.

```bash
docker run -d --network my-net --name web alpine sleep 1000
```
- 4. Verify communication
Execute a ping command from the web container to the db container.

```bash
docker exec -it web ping db
``` 
Expected Results: The web container should resolve db to an internal IP address and receive successful replies:

```plaintext
PING db (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.084 ms
```
- 5. Cleanup
Remove the containers and the network to reset your environment.

```bash
docker rm -f db web
docker network rm my-net
```