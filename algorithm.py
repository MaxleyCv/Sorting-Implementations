import printer
import copy

quicksort_swap_counter = 0

def swap(list_of_things, i, j):
    container = copy.deepcopy(list_of_things[i])
    list_of_things[i] = copy.deepcopy(list_of_things[j])
    list_of_things[j] = copy.deepcopy(container)
    return list_of_things


def selectionsort(list_of_printers, greater_than=True, tag="speed"):
    for i in range(len(list_of_printers)):
        optimum_index = i
        for j in range(i, len(list_of_printers)):
            if printer.Printer.compare(list_of_printers[j], list_of_printers[optimum_index], tag=tag, greater_than=greater_than):
                optimum_index = j
        list_of_printers = swap(list_of_printers, i, optimum_index)
    return list_of_printers

some_list = []

def quicksort(list_of_printers, left_index, right_index):
    if len(list_of_printers) == 1:
        return list_of_printers
    if left_index < right_index:
        pi = quicksort_barier_of_printers_devide(list_of_printers, left_index, right_index)
        quicksort(list_of_printers, left_index, pi - 1)
        quicksort(list_of_printers, pi + 1, right_index)


def quicksort_barier_of_printers_devide(list_of_printers, left_position, right_position):
    current_index = (left_position - 1)
    wavechange_barrier = list_of_printers[right_position].price
    for running_index in range(left_position, right_position):
        if list_of_printers[running_index].price <= wavechange_barrier:
            current_index = current_index + 1
            quicksort_swap_counter += 1
            print(quicksort_swap_counter)
            list_of_printers[current_index], list_of_printers[running_index] = list_of_printers[running_index], list_of_printers[current_index]
    list_of_printers[current_index + 1], list_of_printers[right_position] = list_of_printers[right_position], list_of_printers[current_index + 1]
    return current_index + 1

