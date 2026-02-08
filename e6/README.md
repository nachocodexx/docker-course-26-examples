# Multi-stage build
This example demonstrates how to use multi-stage builds in Docker to create a smaller final image. The first stage builds the application, and the second stage copies only the necessary files to create a lightweight image.

1. Create a new directory for the project and navigate into it:

```bash 