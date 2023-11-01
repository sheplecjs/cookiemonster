FROM python:3.11.4
WORKDIR /cookiemonster 

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN python -m pip install \
        -r requirements.txt