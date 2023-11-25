FROM {{cookiecutter.project_base_image}}
WORKDIR /{{cookiecutter.project_name|lower}}

RUN apt-get update
RUN apt-get install -y tree

# adding rustup
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN python -m pip install \
        -r requirements.txt