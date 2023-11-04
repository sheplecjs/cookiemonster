FROM {{cookiecutter.project_base_image}}
WORKDIR /{{cookiecutter.project_name|lower}}

{% if cookiecutter.project_base_deps == "django/psycopg" -%}
EXPOSE 8000
{%- endif %}

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN python -m pip install \
        -r requirements.txt