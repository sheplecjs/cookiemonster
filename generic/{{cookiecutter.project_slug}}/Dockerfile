FROM {{cookiecutter.project_base_image}}
WORKDIR /{{cookiecutter.project_name|lower}}

RUN apt-get update
RUN apt-get install -y tree

{% if cookiecutter.project_base_deps == "django/psycopg" -%}
EXPOSE 8000
{% elif cookiecutter.project_base_deps == "sam" -%}
RUN wget\ 
    https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
RUN unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
RUN ./sam-installation/install
{%- endif %}

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
RUN python -m pip install --upgrade pip