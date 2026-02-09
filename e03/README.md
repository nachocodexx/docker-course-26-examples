 # Writing a Dockerfile

This directory contains a Dockerfile that can be used to build a Docker image for the E3 project. The Dockerfile is based on the official node image and includes the necessary dependencies to run the E3 application.

## Project structure
The project structure is as follows:

```bash
e3/
├── Dockerfile
├── app.js
└── README.md
```

## Building the Docker image
To build the Docker image, navigate to the `e3` directory and run the following command:
```bash
docker build -t image3 .
```
This command will build the Docker image and tag it as `image3`. The `.` at the end of the command specifies the build context, which is the current directory.
## Running the Docker container
To run the Docker container, use the following command:
```bash
docker run --rm image3
```