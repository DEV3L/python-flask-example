#!/bin/bash

python setup.py develop
py.test > test_results.txt

if grep -q 'FAILURES' test_results.txt ; then
    exit 1
fi
