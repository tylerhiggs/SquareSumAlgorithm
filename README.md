

# Squares Sum Algorithm
## Tyler Higgs, June 2020



1. Sub Problem
    * x(i) = find the smallest number of squared numbers which sum to i

2. Relation

    * x(i) = 1 + min{ x(i-j^2) } ∀ j ∈ {1,...,floor(i^0.5) } 

3. Topological Order

    * i always decreases

4. Base

    * x(0) = 0

5. Original

    * x(n) gives the fewest number of square integers which sum to n

6. Time

    * O(n) sub problems
    * O(\sqrt{n}) work done per sub problem
    * O(n\sqrt{n}) run-time

