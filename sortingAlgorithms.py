# Author: Edwin Onyango
# Date: 27th Aug 2022
# Purpose: Generating a class for the different sorting algorithms:

# class declaration:
class SortingAlgorithms:
    # Method declarations

    # Constructor
    def __init__(self, list_to_sort) -> None:
        self.list_to_sort = list_to_sort

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
                temp = self.list_to_sort[pos]
                self.list_to_sort[pos] = self.list_to_sort[last_min]
                self.list_to_sort[last_min] = temp
            
        return self.list_to_sort
                
