# Exercise 1: Create an image

This script will run a Docker container with the name "container1" using the Ubuntu image in interactive mode (-ti).


1. In a terminal, run the following command to start a new container:
```bash
docker run --name=container1 -ti ubuntu
```

2. Once you are inside the container, update the package list and install Node.js by running the following command:

```bash
 apt update && apt install -y nodejs
``` 

When this command runs, it downloads and installs Node inside the container. In the context of the union filesystem, this means that the Node.js files are added to the container's filesystem layer. The container can now use Node.js as if it were installed on a regular system, but it is actually running in an isolated environment provided by Docker.

3. After the installation is complete, you can verify that Node.js is installed by running:

```bash
node -e "console.log('Node.js is installed')"
```


4. Now commit the changes you made to the container to create a new image. In another terminal, run the following command:

```bash
docker commit -m "add nodejs" container1 image1
```

5. Check history of the new image to see the commit message:

```bash
docker history image1

fc674838ad3b   21 seconds ago   /bin/bash                                       160MB     add nodejs
493218ed0f40   3 weeks ago      /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
<missing>      3 weeks ago      /bin/sh -c #(nop) ADD file:3077ee44db3cc7d38…   78.1MB
<missing>      3 weeks ago      /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
<missing>      3 weeks ago      /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
<missing>      3 weeks ago      /bin/sh -c #(nop)  ARG LAUNCHPAD_BUILD_ARCH     0B
<missing>      3 weeks ago      /bin/sh -c #(nop)  ARG RELEASE                  0B
```

6. To prove that the new image contains Node.js, run a container from the new image and check the Node.js version:

```bash
docker run --rm image1 node -v
```