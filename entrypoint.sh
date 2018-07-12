#!/usr/bin/env sh

if [[ ! -r ./adapter.py ]]; then
    echo "The adapter file is missing!";
    exit 1;
fi

if [[ ! -r ./sample.py ]]; then
    echo "The sample file is missing!";
    exit 2;
fi

if [[ ! -r ./solution.py ]]; then
    echo "The solution file is missing!";
    exit 3;
fi

if [[ ! -r ./testdata.json ]]; then
    echo "The options file is missing!";
    exit 4;
fi

if [[ ! -w ./result.json ]]; then
    echo "The result file is missing!";
    exit 5;
fi

./main.py
