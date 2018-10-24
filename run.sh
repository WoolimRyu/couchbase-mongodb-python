#!/bin/bash -e

function abspath() {
    python -c "import os;print os.path.abspath( '$1' )"
}

CWD=`abspath $(dirname $0)`
APP_HOME=`abspath $CWD`
VENV=`abspath $APP_HOME/venv`

function setup() {
    virtualenv $VENV --no-site-packages
    source $VENV/bin/activate
    #PIP_OPTS="--trusted-host ftp.daumkakao.com --index-url=http://ftp.daumkakao.com/pypi/simple/"
    python $VENV/bin/pip install $PIP_OPTS -r $CWD/req.txt
}

function all() {
    cd $CWD
    source $VENV/bin/activate
    python ./app/data_check.py
}


$1
