# Author: Edwin Onyango
# Date: 27th Aug 2022
# Purpose: Generating a class for the different sorting algorithms:

# class declaration:
from heapq import heapify

class SortingAlgorithms:
    # Method declarations

    # Constructor
    def __init__(self, list_to_sort) -> None:
        self.list_to_sort = list_to_sort

    # since a swap appears a lot, i decided to generate a function
    def swap_list_vals(self, list, pos1, pos2):
        # swap
        list[pos1], list[pos2] = list[pos2], list[pos2]

    ################### selection_sort #########################
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

    ################# bubble_sort #################
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

    ################ insertion_sort ################        
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

    ############# merge_sort and helper ####################
    def merge_sort(self):
        list = self.list_to_sort
        list = self.merge_helper2(list)
        return list

    def merge_helper2(self, list_to_sort):
        # recursive call after splitting the list into two
        mid_point = len(list_to_sort)/2

        left_list = list_to_sort[:int(mid_point)]
        right_list = list_to_sort[int(mid_point):]
        print(left_list, ",,,,,,,,", right_list)

        # call merge_sort recursively
        if(len(right_list) > 1):
            right_list = self.merge_helper2(right_list)
        if(len(left_list) > 1):
            left_list = self.merge_helper2(left_list)

        # Once the length is one, merge based on values:
        return self.merge_helper(right_list, left_list)

    # merge list 1 into list 2
    def merge_helper(self, list1, list2):
        start_point = 0

        # bring the two lists together
        for i in range(len(list1)):
            if(start_point == len(list2)):
                list2.extend(list1)
                return list2
            
            while((start_point < len(list2)) and (list1[i] > list2[start_point])):
                start_point += 1
            
            if(start_point >= len(list2)):
                list2.append(list1[i])
            else:
                list2.insert(start_point, list1[i])

        # return the merged list
        return list2

  ############# quick_sort and helper ####################
    def quick_sort(self):
        sorted_list = self.quick_sort_helper(self.list_to_sort)
        return sorted_list

    def quick_sort_helper(self, list):
        if(len(list) <= 1):
            return list
        print(len(list))
        pivot_num = list[(len(list) - 1)]

        # swap any bigger numbers to move to the end and ignore smaller then return specific pos
        mid = -1
        for i in range(len(list)):
            if(list[i] <= pivot_num):
                # swap it's position into mid and increment:
                mid += 1
                self.swap_list_vals(list, mid, i)
        
        left_list = list[:mid]
        right_list = list[mid:] 

        print(right_list, ",,,,,,,,,,,", left_list)
        left_list = self.quick_sort_helper(left_list)
        right_list = self.quick_sort_helper(right_list)

        # Combine two lists
        if((right_list != None) and (left_list != None)):
            left_list = left_list.extend(right_list)
        print(left_list)

        return left_list

    ############# heap_sort and helpers ####################
    def heap_sort(self):
        # makes use of the nice heap structure
        # heapify then continously take min to the end while decreasing size of the heap
        heap_size  =  len(self.list_to_sort)
        list = self.list_to_sort

        heapify(list)

        print(list, "heaped")
        while(heap_size > 1):
            self.helper_maintain_heap(list, heap_size, 0)
            # swap the root with the last element
            print("new min picked")
            print("heap before swap")
            print(list)
            print(heap_size)
            list[0], list[heap_size -1] = list[heap_size -1], list[0]
            print(list)
            heap_size -= 1
        
        returned_list = list[::-1]
        return returned_list

    def helper_maintain_heap(self, heap, heap_size, pos):
        # maintain min on top
        smallest = pos
        left = 2 * pos + 1
        right = 2 * pos + 2
        if(left < heap_size and heap[smallest] > heap[left]):
            # point to smallest
            smallest = left
        if(right < heap_size and heap[smallest] > heap[right]):
            # point to smallest
            smallest = right
        
        if(smallest != pos):
            # swap positions
            heap[smallest], heap[pos] = heap[pos], heap[smallest]
            print(heap)
            # maintain heap value property
            self.helper_maintain_heap(heap, heap_size, smallest)
            