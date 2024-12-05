#!/bin/bash
set -euo pipefail

IN=$1

awk '{print $1}' $IN | sort -n > /tmp/l

awk '{print $2}' $IN | sort -n > /tmp/r

sum=0

while read l r
do
    if [[ $r > $l ]]
    then
        d=$(( $r - $l ))
    else
        d=$(( $l - $r ))
    fi

    sum=$(( $sum + $d ))
done < <( paste /tmp/l /tmp/r )

echo ${sum}
