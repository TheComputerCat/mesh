FROM python:bookworm

RUN useradd -m user

WORKDIR /home/user

USER user

RUN pip install debugpy

EXPOSE 5678

CMD [ "/bin/bash" ]