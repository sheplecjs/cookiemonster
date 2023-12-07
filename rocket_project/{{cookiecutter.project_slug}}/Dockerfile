FROM rust:latest

RUN rustup component add rustfmt

WORKDIR /usr/src/myapp
COPY . .

RUN cargo install --path .