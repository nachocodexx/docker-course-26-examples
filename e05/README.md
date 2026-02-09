# Layers caching
This example shows how to cache layers in a registry and reuse them across builds. This can speed up builds significantly, especially when the same layers are used in multiple images.


1. First we will create a Dockerfile that installs Python and pip. Create a file named `Dockerfile` with the following content:

```Dockerfile
FROM python:3.9
COPY requirements.txt .
COPY src/ .
RUN pip install -r requirements.txt 
CMD ["python3", "app.py"]
```

2. Next, we will create a `requirements.txt` file that lists the Python dependencies for our application. Create a file named `requirements.txt` with the following content:

```
numpy
```

3. Now we will build the Docker image using the Dockerfile. Run the following command in the terminal:

```bash
docker build -t cache_example .
```

4. After the build is complete, we can check the layers of the image using the `docker history` command:

```bash
docker history cache_example
```

5. Now we will run the container to verify that it works:

```bash
docker run --rm cache_example
```