# Build, tag and push the Docker image



To build, tag, and push the Docker image for the E4 project, follow these steps:

1. **Build the Docker image**: Navigate to the `e4` directory and run the following command to build the Docker image:

   ```bash
   docker build -t <username>/image4 .
   ```

   This command will build the Docker image and tag it as `<username>/image4`. The `.` at the end of the command specifies the build context, which is the current directory.  


2. **Push the Docker image to Docker Hub**: After building the image, you can push it to Docker Hub using the following command:

   ```bash
   docker push <username>/image4
   ```