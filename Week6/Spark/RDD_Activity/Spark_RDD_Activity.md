# Spark RDD Activity

## Goal

- Practice RDD operations.

## Solve the following

1) Consider the following lists:

    ```
    [1, 2, 3, 4, 5, 6]
    [1, 3, 5, 7, 9]
    ```

    Parallelize these lists into two separate RDDs. Create a new RDD that contains the data that is common to both lists. Print to the console.

2) Consider this list of coordinates:

    ```
    [(33.245, 22.456), (-15.321, 28.123), (62.453, -5.265), (28.443, 23.543), (72.344, -25.352), (45.234, 23.234), (-40.233, -28.987)]
    ```

    Load this list into an RDD. Sort the list by distance from (38.898, 77.037). Print to the console.

3) Load pokemon.csv into an RDD. Transform the RDD to get a list of generations as well as the count of how many pokemon are in each generation and their average attack.

    - (hint: use map to create a new RDD with key-value pairs (the value can be a data collection itself) which will allow you to use reduceByKey() ).
