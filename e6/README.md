# Multi-stage build
This example demonstrates how to use multi-stage builds in Docker to create a smaller final image. The first stage builds the application, and the second stage copies only the necessary files to create a lightweight image.


1. Create a new directory for this exercise and navigate into it:
```bash
mkdir src
```

2. Inside the `src` directory, create a new Rust source file named `main.rs` with the following content:

```rust
fn main() {
    println!("Hello, world!");
}
```

3. Create a `Dockerfile` in the root of the exercise directory with the following content:

```Dockerfile
FROM rust:latest AS builder
WORKDIR /app
COPY src/ ./src
COPY Cargo.toml .

RUN cargo build --release

FROM debian:bookworm-slim
WORKDIR /app
COPY --from=builder /app/target/release/hello_world .
CMD ["./hello_world"]
```
4. Build the Docker image using the following command:

```bash
docker build -t ms_rust .
```

Check history of the new image to see the layers:

```bash 
docker history ms_rust
``` 

5. Run a container from the newly built image to verify that it works:

```bash
docker run --rm ms_rust
```
