from printer import *
import algorithm
import random
import sys
import utils
import time
import copy
import csv_reader as inp

'''
getting filename from the command prompt
'''
if len(sys.argv) > 1 and (not ("display-elements=false" in sys.argv) or len(sys.argv) > 2):
    utils.INPUT_FILE = str(sys.argv[1])
    print(utils.INPUT_FILE)

if "display-elements=false" in sys.argv:
    utils.DISPLAY_VALUES = False

if __name__ == "__main__":
    list_of_printers = []
    if utils.INPUT_FILE == "default":
        count_of_random_array = 0
        print("RANDOM ARRAYS WILL BE TAKEN:")
        print("PLEASE SELECT NUMBER OF ITEMS: ")
        try:
            count_of_random_array = int(input())
        except:
            print("INVALID DATA, ABORTING ...")
            exit()

        for i in range(count_of_random_array):
            list_of_printers.append(Printer("Canon", random.randint(1, 100), random.randint(4000, 40000)))
    else:
        print("VALUES WILL BE TAKEN FROM " + utils.INPUT_FILE)
        list_of_printers = inp.get_printers_from_file()

    if utils.DISPLAY_VALUES:
        for printer in list_of_printers:
            print(printer)

    list_for_selection = copy.deepcopy(list_of_printers)
    list_for_qsort = copy.deepcopy(list_of_printers)


    print("#############################################")
    print("          SELECTION SORT BY SPEED            ")
    print("#############################################")
    selection_time_start = time.time()
    list_of_printers = algorithm.selectionsort(list_for_selection)
    selection_time = time.time() - selection_time_start
    print("TIME FOR SORTING: " + str("%.4f" % (selection_time * 10000)) + " ms")
    print("SWAPS: " + str(utils.select_swap_counter))
    print("COMPARES: " + str(utils.select_comp_counter))
    print("#############################################")

    if utils.DISPLAY_VALUES:
        for printer in list_for_selection:
            print(str(printer))

    print("#############################################")
    print("          QUICKSORT SORT BY PRICE            ")
    print("#############################################")
    qsort_start = time.time()
    algorithm.quicksort(list_for_qsort, 0, len(list_for_qsort) - 1)
    qsort_time = time.time() - qsort_start
    print("TIME FOR SORTING: " + str("%.4f" % (qsort_time * 1000)) + " ms")
    print("SWAPS: " + str(utils.qsort_swap_counter))
    print("COMPARES: " + str(utils.qsort_compare_counter))
    print("#############################################")

    if utils.DISPLAY_VALUES:
        for printer in list_for_qsort:
            print(str(printer))

