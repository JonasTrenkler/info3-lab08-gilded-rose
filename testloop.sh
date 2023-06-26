#!/bin/zsh

echo "-----1: ----$1"
if [ $1 ]; then
    subdir=$1
else
    subdir=tests
fi
# echo "-----subdir: ----$subdir"

while true; do
    clear
    # use this to stop at first failure:
    # pytest -x -vv $subdir
    pytest -vv -rxX $subdir --ignore=$subdir/examples
    fswatch ./**/*.py  -1
done

#-r chars              Show extra test summary info as specified by chars: (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed, (p)assed, (P)assed with output, (a)ll except passed (p/P), or (A)ll. (w)arnings are enabled by default (see --disable-warnings), 'N' can be used to reset the list. (default: 'fE').
