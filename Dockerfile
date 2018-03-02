FROM python:3

LABEL maintainer="b.eyselein@gmail.com"

ARG WorkDir=/data

# Add base files folder to python path
ENV PYTHONPATH $WorkDir/base:$PYTHONPATH

WORKDIR $WorkDir

COPY ./base $WorkDir/base
COPY ./*.py $WorkDir/

ENTRYPOINT ["bash"]