FROM python:3

WORKDIR /data

COPY ./base /data/base
COPY ./*.py /data/

ENTRYPOINT ["bash"]