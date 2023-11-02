FROM python:3.11.4
WORKDIR /cookiemonster 

RUN git config --global user.email sheplecjs@pm.me
RUN git config --global user.name Colin Shepley

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN python -m pip install \
        -r requirements.txt