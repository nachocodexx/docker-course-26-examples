# Exercise 2: Create a Dockerfile and build an image

Now that you have create an image with Node.js installed, let's build a image.

1. Start a new container using the new image you created in Exercise 1:

```bash
docker run --name=container2 -ti image1
```

2. Inside of this container, run the following command to create a new file called "app.js" with the following content:


```bash
echo "console.log('Hello from Node.js');" > app.js
```

To run this file, you can use the following command:

```bash
node app.js
```

3. In another terminal, commit the changes you made to the container to create a new image:

```bash
docker commit -c 'CMD ["node", "app.js"]' -m "Add app.js" container2 image2

IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
2f2d81f3018e   1 second ago    /bin/bash                                       35B       Add app.js
fc674838ad3b   9 minutes ago   /bin/bash                                       160MB     add nodejs
493218ed0f40   3 weeks ago     /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
<missing>      3 weeks ago     /bin/sh -c #(nop) ADD file:3077ee44db3cc7d38…   78.1MB
<missing>      3 weeks ago     /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
<missing>      3 weeks ago     /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
<missing>      3 weeks ago     /bin/sh -c #(nop)  ARG LAUNCHPAD_BUILD_ARCH     0B
<missing>      3 weeks ago     /bin/sh -c #(nop)  ARG RELEASE                  0B
```

This command creates a new image called "image2" with the changes you made to the container, and also sets the default command to run when a container is started from this image to "node app.js".

4. To verify that the new image works as expected, run a container from the new image:

```bash
docker run --rm image2
```