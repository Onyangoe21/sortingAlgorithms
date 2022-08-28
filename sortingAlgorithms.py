# Author: Edwin Onyango
# Date: 27th Aug 2022
# Purpose: Generating a class for the different sorting algorithms:

# class declaration:
class SortingAlgorithms:
    # Method declarations

    # Constructor
    def __init__(self, list_to_sort) -> None:
        self.list_to_sort = list_to_sort

    # since a swap appears a lot, i decided to generate a function
    def swap_list_vals(self, list, pos1, pos2):
        temp = list[pos1]
        list[pos1] = list[pos2]
        list[pos2] = temp

    # selection sort checks for all mins individually and arranges them:
    def selection_sort(self):
       

        # loop whole list
        for pos in range(len(self.list_to_sort)):
            # see if current index is the min and place accordingly
            last_min = pos # record position to use for swap
            tracker = pos
            min = self.list_to_sort[pos]  # Set min to current element
            while(tracker < len(self.list_to_sort)): # always start at pos forwards
                
                if (min > self.list_to_sort[tracker]):
                    print("new min of ", self.list_to_sort[tracker]," detected for pos ", pos,".")
                    last_min = tracker
                    min = self.list_to_sort[tracker]
                
                tracker += 1
            
            # bring most min value forward by swap if the value changed
            if(last_min != pos):
                #swap
                print(self.list_to_sort[pos], "is about to be swapped with", self.list_to_sort[last_min])
                self.swap_list_vals(self.list_to_sort, pos, last_min)
                
            
        #return self.list_to_sort

    # bubble sort implementation
    def bubble_sort(self):

        swap_happened = True

        while(swap_happened):
            swap_happened = False # set to false to detect if a swap happened
            # loop whole list
            # swap if a number is smaller
            for pos in range(len(self.list_to_sort) - 1):
                if(self.list_to_sort[pos] > self.list_to_sort[pos + 1]):
                    print("value swap:")
                    swap_happened = True
                    self.swap_list_vals(self.list_to_sort, pos, pos + 1)

    # insertion sort implementation        
    def insertion_sort(self):
        # compare elements and if sorted in relation to the next one, add to sorted sub-array else keep swapping and comparing

        start_of_unordered = 0
        while(start_of_unordered < len(self.list_to_sort) - 1):
            # loop from un-ordered section of array comparing to last element of the sorted portion
            if(self.list_to_sort[start_of_unordered] > self.list_to_sort[start_of_unordered + 1]):
                self.swap_list_vals(self.list_to_sort, start_of_unordered, start_of_unordered + 1)

            if(start_of_unordered > 0 and self.list_to_sort[start_of_unordered - 1] > self.list_to_sort[start_of_unordered]):
                print("a smaller element of", self.list_to_sort[start_of_unordered],"and", self.list_to_sort[start_of_unordered - 1], "is no longer ordered")
                start_of_unordered -= 1
            else:
                start_of_unordered += 1   