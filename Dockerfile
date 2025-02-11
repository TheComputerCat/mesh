FROM python:bookworm

RUN useradd -m user

WORKDIR /home/user

USER user