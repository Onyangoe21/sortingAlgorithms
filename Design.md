# Sorting Algorithms Design document
# Personal project
# Author: Edwin Omondi Onyango



The **sortingAlgorithms** is responsible for implementing the different sorting algorithms in python.
It details the code and parameter usage.

This design spec will include the following: 

* Inputs and Outputs
* Functional decomposition into modules
* Pseudo code for logic/algorithmic flow
* Dataflow through modules
* Usage instructions
* Testing plan

## Pseudo code for logic/algorithmic flow

### selection_sort()
* This sorting method involves searching for min value every time and putting it in the current position. The runtime complexity is Big Theta(n squared).
* In this repo, it is simplly implemented by looping all elements and on each, finding if it is the min value in the whole remaining portion of the list and then inserting it

### bubble_sort()
* This sorting method involves swapping value for next one if it's greater and repeating the same until no more swaps have been noted. The runtime complexity is Big O(n squared): 
``` runs n-1 times each loop and in worst case scenario, sorting in ascending order involves the smallest number at end of list that has to be bubbled in n-1 runs: Thus, worst case is (n-1)*(n-1) ```

* Big Omega(n)-- for in best case scenario, list is sorted and it loops it all with no change

### insertion_sort()
* This sorting method involves inserting value a current ordered portion provided it is greater than what is before and smaller thank next value. Otherwise, the value is not ordered and ordered portion becomes smaller to allow swaps. The runtime complexity is Big O(n squared): 
``` runs at most n-1 for a single value, assuming the value is smallest and at the end and subsequently one lesser for each of the other values in other positions in the list.This leads to the sum 1 + 2 + ... n-2 + n-1 = (n-1)(n-1 + 1)/2: but this is  n(n-1)/2:```

* Big Omega(n)-- for in best case scenario, list is sorted and it loops n - 1 times confirming that each value is ordered

### merge_sort()
* This sorting method involves a "divide and conquer strategy where the list is continuously split into 2 until length 1 and then merged again based on which elements are bigger. This is done recursively in this implementation. As for the runtime complexity, the algorithmic flow is such that: 
``` List is continusly split into 2: ```
    ```(This is O(log(n)) --- base 2) ```
    ```For each of these is a merge function that brings together both sides: it does it by performing extend or insert into the list and since insert is O(n) and extend is O(m) where m is length of 2nd list, the maximum number of times this can run is O(nlog(n)): This is an oversimplified way of saying it so, For more details on how this is reached, this recurrence relation takes the form of T(n) = 2T(n/2) + θ(n), which, if solved using the Master method, results to the answer above and show why you could say the same about the lower bound.```

* Big Theta(n log n)-- explained above

