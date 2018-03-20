#!/bin/bash
path=`dirname $0`
binary="$path/../computor.py"

polynomials=(
	# subject
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    "5 * X^0 + 4 * X^1 = 4 * X^0"
    "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"

	# complex solutions
    "1 * X^0 + 1 * X^1 + 1 * X^2 = 0"
    "1 * X^0 + 1 * X^1 + 1 * X^2 = 0 * X^0"

	# reduced form
    "0.0 * X^0 + 7.5 * X^1 - 5163.4 * X^2 = 0"

	# various tests
    "0.0 * X^0 + 7.5 * X^1 - 5163.4 * X^2 = 3 * X^0"
    "0.0000 * X^0 = 0"
    "0 * X^0 = 0"
    "1 * X^0 + 0 * X^1 + 1 * X^2 = 0"
    "4 * X^0 + 0 * X^1 + 1 * X^2 = 0"
    "1 * X^0 - 1 * X^1 = 0"
    "1 * X^0 - 4 * X^1 = 0"
    "3 * X^0 - 6 * X^1 + 3 * X^2 = 0"

    "3 * X^0 = 0"
    "0.0001 * X^0 = 0"

    "1 * X^0 + 1 * X^1 + 1 * X^2 + 1 * X^3 + 1 * X^4 = 0"
    "1 * X^0 + 1 * X^1 + 1 * X^ 2 + 1 * X^3 + 1 * X^4 + 1 * X^5 = 0"

    "1 * X^0 + 1 * X^1 + 1 * X^2 + 1 * X^3 + 1 * X^4 = -2 * X^4"
	"1 * X^0 + 1 * X^2 = 0"
    "0 = 0"
    "0.0 * X^0 + 7.5 * X^1 - 5163.4 * X^2 = 3"
    "qeokoh djdgoerjg   "
    "0 * X^3 +qeokoh djdgoerjg   "
)

nb_poly=${#polynomials[@]}
let "last_poly = $nb_poly - 1"
for i in `seq 0 $last_poly`
do
    command="$binary \"""${polynomials[$i]}\""
    echo "$command"
    eval "$command"
    if [ $i != $last_poly ]
    then
        echo ""
    fi
done
