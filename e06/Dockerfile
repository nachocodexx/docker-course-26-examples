FROM rust:latest AS builder
WORKDIR /app
COPY src/ ./src
COPY Cargo.toml .

RUN cargo build --release

FROM debian:bookworm-slim
WORKDIR /app
COPY --from=builder /app/target/release/hello_world .
CMD ["./hello_world"]