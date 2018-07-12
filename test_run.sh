#!/usr/bin/env bash

docker run -it --rm \
    -v ~/workspace/robots/adapter.py:/data/adapter.py \
    -v ~/workspace/robots/solution.py:/data/solution.py \
    -v ~/workspace/robots/sample.py:/data/sample.py \
    -v ~/workspace/robots/testdata.json:/data/testdata.json \
    -v ~/workspace/robots/result.json:/data/result.json \
    beyselein/py_rose

cat result.json