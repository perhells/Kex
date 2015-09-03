for COUNT in 100 1000 10000 100000 500000 1000000
do
    echo $COUNT runs
    python main.py $COUNT data > results/$COUNT
done
