from sortingAlgorithms import SortingAlgorithms
# Test class creation
list = [34, 56, 12, 1, -1, 90, 45, 3, 12, 25]
print("###################   selection_sort    ####################################")
list_sorter = SortingAlgorithms(list)

print("Now testing the selection sort")
# print list before sorting
print("list before sorting")
print(list)

# print list after sorting
list_sorter.selection_sort()

print("list after sorting")
print(list)
#############################################################

print("###########################   bubble_sort   ############################")
list = [34, 56, 12, 1, -1, 90, 45, 3, 12, 25]
list_sorter = SortingAlgorithms(list)

print("Now testing the bubble sort")
# print list before sorting
print("list before sorting")
print(list)

# print list after sorting
list_sorter.bubble_sort()

print("list after sorting")
print(list)

#############################################################

print("#########################   insertion_sort   ########################")
list = [34, 56, 12, 1, -1, 90, 45, 3, 12, 25]
list_sorter = SortingAlgorithms(list)

print("Now testing the insertion sort")
# print list before sorting
print("list before sorting")
print(list)

# print list after sorting
list_sorter.insertion_sort()

print("list after sorting")
print(list)

print("#########################   merge_sort   ########################")
list = [34, 56, 12, 1, -1, 90, 45, 3, 12, 25]
list_sorter = SortingAlgorithms(list)

print("Now testing the merge sort")
# print list before sorting
print("list before sorting")
print(list)

# print list after sorting
list = list_sorter.merge_sort()

print("list after sorting")
print(list)

print("#########################   quick_sort   ########################")
list = [34, 56, 12, 1, -1, 90, 45, 3, 12, 25]
list_sorter = SortingAlgorithms(list)

print("Now testing the quick sort")
# print list before sorting
print("list before sorting")
print(list)

# print list after sorting
list = list_sorter.quick_sort()

print("list after sorting")
print(list)

print("#########################   heap_sort   ########################")
list = [34, 56, 12, 1, -1, 90, 45, 3, 12, 25]
list_sorter = SortingAlgorithms(list)

print("Now testing the quick sort")
# print list before sorting
print("list before sorting")
print(list)

# print list after sorting
list = list_sorter.heap_sort()

print("list after sorting")
print(list)