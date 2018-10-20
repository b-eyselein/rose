#!/usr/bin/env bash

docker run -it --rm --name rose_new_test \
    -v ${PWD}/options.json:/data/options.json \
    -v ${PWD}/solution.py:/data/solution.py \
    -v ${PWD}/new_actions.json:/data/actions.json \
    rose_new