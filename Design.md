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