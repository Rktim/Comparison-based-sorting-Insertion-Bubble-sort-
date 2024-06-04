# Comparison-based-sorting-Insertion-Bubble-sort.

Pseudocodes:

1. Insertion Sort:
       function insertionSort(array)
       for i in range(1, len(array)):
          key = array[i]
          j = i - 1
          while j >= 0 and array[j] > key:
              swap(array[j + 1], array[j])
              j -= 1
        swap (array[j + 1] ,key)
        return array

2. Bubble sort
       function bubbleSort(array)
        n = len(array)
        for i in range(n - 1):
             for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                   swap(array[j], array[j + 1] )
        return array

   
