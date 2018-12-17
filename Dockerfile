FROM python@sha256:abc2a66d8ce0ddf14b1d51d4c1fe83f21059fa1c4952c02116cb9fd8d5cfd5c4

LABEL maintainer="b.eyselein@gmail.com"

ARG WorkDir=/data

# Add base files folder to python path
ENV PYTHONPATH $WorkDir/base:$PYTHONPATH

WORKDIR $WorkDir

COPY . $WorkDir/

ENTRYPOINT ./sp_main.py