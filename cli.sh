#!/bin/bash -x

<<COMMENTOUT
oj login https://atcoder.jp/contests             # login
acc new abc252 -c all                            # download
oj t -c 'python3 main.py' -d ./tests/            # test
acc s main.py -- --guess-python-interpreter pypy -w 0 -y # submit
COMMENTOUT

COMMAND_L="oj login https://atcoder.jp/contests"
COMMAND_D="acc new abc252 -c all"
COMMAND_T="oj t -c 'python3 main.py' -d ./tests/"
COMMAND_S="acc s main.py -- --guess-python-interpreter pypy -w 0 -y"

COMMAND=""
while getopts ld:ts OPT
do
  case $OPT in
    l ) echo "l" ;COMMAND="${COMMAND_L}" ;;
    d ) ABCNO="$OPTARG";COMMAND="acc new abc${ABCNO} -c all" ;;
    t ) COMMAND="${COMMAND_T}" ;;
    s ) COMMAND="${COMMAND_S}" ;;
    * ) echo "no function!!" ;;
  esac
done

if [ "${COMMAND}" == "" ]; then
    echo ${COMMAND_L}
    echo ${COMMAND_D}
    echo ${COMMAND_T}
    echo ${COMMAND_S}
    exit 0
fi

echo "---"
echo ${COMMAND}
echo "---"
${COMMAND}
