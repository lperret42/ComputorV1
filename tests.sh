binary="./computor.py"

polynomials=(
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    "5 * X^0 + 4 * X^1 = 4 * X^0"
    "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
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
