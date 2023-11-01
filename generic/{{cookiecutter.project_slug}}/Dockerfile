FROM {{cookiecutter.project_base_image}}
WORKDIR /{{cookiecutter.project_name|lower}}

RUN git config --global user.email {{cookiecutter.email}}
RUN git config --global user.name {{cookiecutter.full_name}}

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN python -m pip install \
        -r requirements.txt