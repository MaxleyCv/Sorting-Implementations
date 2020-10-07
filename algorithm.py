import printer
import copy
import utils


def swap(list_of_things, i, j):
    container = copy.deepcopy(list_of_things[i])
    list_of_things[i] = copy.deepcopy(list_of_things[j])
    list_of_things[j] = copy.deepcopy(container)
    return list_of_things


def selectionsort(list_of_printers, greater_than=True, tag="speed"):
    for i in range(len(list_of_printers)):
        optimum_index = i
        for j in range(i, len(list_of_printers)):
            utils.select_comp_counter += 1
            if printer.Printer.compare(list_of_printers[j], list_of_printers[optimum_index], tag=tag, greater_than=greater_than):
                optimum_index = j
        list_of_printers = swap(list_of_printers, i, optimum_index)
        utils.select_swap_counter += 1
    return list_of_printers


def quicksort(list_of_printers, left_index, right_index):
    if len(list_of_printers) == 0: return
    utils.qsort_compare_counter += 1
    if len(list_of_printers) == 1:
        return list_of_printers
    utils.qsort_compare_counter += 1
    if left_index < right_index:
        new_barrier = set_the_barrier(list_of_printers, left_index, right_index)
        quicksort(list_of_printers, left_index, new_barrier - 1)
        quicksort(list_of_printers, new_barrier + 1, right_index)


def set_the_barrier(list_of_printers, left_position, right_position):
    current_index = (left_position - 1)
    wavechange_barrier = list_of_printers[right_position].price
    for running_index in range(left_position, right_position):
        utils.qsort_compare_counter += 1
        if list_of_printers[running_index].price <= wavechange_barrier:
            current_index = current_index + 1
            utils.qsort_swap_counter += 1
            swap(list_of_printers, current_index, running_index)
    swap(list_of_printers, current_index + 1, right_position)
    utils.qsort_swap_counter += 1
    current_index += 1
    return current_index

