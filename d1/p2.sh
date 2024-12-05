#!/bin/bash
set -euo pipefail

IN=$1

awk '{print $1}' $IN | sort -n > /tmp/l

awk '{print $2}' $IN | sort -n > /tmp/r

awk '
    BEGIN { t = 0 }
    FNR==NR { a[$1]++; next }
    FNR!=NR { t = t + ( $1 * a[$1] ) }
    END { print t }
' /tmp/r /tmp/l
