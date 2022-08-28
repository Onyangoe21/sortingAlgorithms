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
