FROM {{cookiecutter.project_base_image}}
WORKDIR /{{cookiecutter.project_name|lower}}

RUN apt-get update
RUN apt-get install -y tree

# adding rustup
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN source "$HOME/.cargo/env"