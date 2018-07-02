FROM python@sha256:5a2deb631d2526a3a6b7226917ee32dc419b95dc1c12267d4562a8c8744a7388
#FROM python:3-alpine

LABEL maintainer="b.eyselein@gmail.com"

ARG WorkDir=/data

# Add base files folder to python path
ENV PYTHONPATH $WorkDir/base:$PYTHONPATH

WORKDIR $WorkDir

COPY ./base $WorkDir/base
COPY ./*.py $WorkDir/
# COPY ./options.json $WorkDir/

ENTRYPOINT ["bash"]
