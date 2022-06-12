#!/bin/bash -x

alias python=python3
alias act="oj t -c 'python3 main.py' -d ./tests/"
alias acs="acc s main.py -- --guess-python-interpreter pypy -w 0 -y"

echo "alias python=python3"
echo "alias act='oj t -c 'python3 main.py' -d ./tests/'"
echo "alias acs='acc s main.py -- --guess-python-interpreter pypy -w 0 -y'"
