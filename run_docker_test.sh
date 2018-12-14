#!/usr/bin/env bash

ACTIONS_FILE=actions.json

if [[ ! -f ${ACTIONS_FILE} ]]; then
    touch ${ACTIONS_FILE}
fi

docker run -it --rm --name rose_new_test \
    -v ${PWD}/options.json:/data/options.json \
    -v ${PWD}/solution_robot.py:/data/solution_robot.py \
    -v ${PWD}/sample_robot.py:/data/sample_robot.py \
    -v ${PWD}/${ACTIONS_FILE}:/data/actions.json \
    rose_new