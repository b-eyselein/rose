FROM python:3-alpine

LABEL maintainer="b.eyselein@gmail.com"

ARG WorkDir=/data

# Add base files folder to python path
ENV PYTHONPATH $WorkDir/base:$PYTHONPATH

WORKDIR $WorkDir

COPY . $WorkDir/

ENTRYPOINT ./sp_main.py