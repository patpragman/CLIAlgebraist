#!/bin/bash

source /home/patrickpragman/PycharmProjects/CLIAlgebraist/venv/bin/activate
str="$*"
python /home/patrickpragman/PycharmProjects/CLIAlgebraist/main.py $str
deactivate
