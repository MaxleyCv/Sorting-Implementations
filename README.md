# Practical work #1
##
## Task
Sort an array of printers in two ways:
- sort by printing speed with selection sort from high to low
- sort by price with quicksort from low to high

Printer object contains 3 fields:
- name (should be str)
- printing speed (in sheets per minute)
- price in UAH

## Manual
In order to check the algorithm there are two options:
- to take values from *.csv* file
- to generate the values randomly  

In order to take values from *.csv* file run command  
 ```python main.py filename.csv```  

Else the number of random array elements will be asked after running
```python main.py```

In order to not to show all the elements in the terminal  
 (especially when there are 1000 of them)  
 add the tag ```display-elements=false``` to the command.
 
##Output
In the output you will get:
- time needed for the sorting algorithm
- number of swaps during the runtime
- number of compares during the runtime
- sorted array if the tag ```display-elements=false``` wasn't added  

Output example:
```
#############################################  
          SELECTION SORT BY SPEED            
#############################################
TIME FOR SORTING: 2556.8604 ms
SWAPS: 1000
COMPARES: 500500
#############################################
#############################################
          QUICKSORT SORT BY PRICE            
#############################################
TIME FOR SORTING: 310.4699 ms
SWAPS: 5693
COMPARES: 13925
#############################################

```