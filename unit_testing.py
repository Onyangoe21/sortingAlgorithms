from sortingAlgorithms import SortingAlgorithms
# Test class creation
list = [34, 56, 12, 1, -1, 90, 45, 3, 12, 25]

list_sorter = SortingAlgorithms(list)

print("Now testing the selection sort")
# print list before sorting
print("list before sorting")
print(list)

# print list after sorting
print(list_sorter.selection_sort())
