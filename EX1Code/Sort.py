# Sort Compare
# This version of Sort Compare uses global variables 
# to store the statistics for a set of numbers using a given sort

import sys





class SortStatistics:
    def __init__(self, **kwargs):
        self.comparisons = 0
        self.swaps = 0
        self.extra_bytes = 0
        self.sortType = kwargs.get("sortType")
        self.nums = kwargs.get("nums")

    def __str__(self):
        # not sure how to do this one
        output =  (f"{self.sortType} Results\n")
        output += (f"Sorted numbers: {self.nums}\n")
        output += (f"Comparisons: {self.comparisons}\n")
        output += (f"Swaps: {self.swaps}\n")
        output += (f"Extra Bytes: {self.extra_bytes}\n")

        return output



# Read numbers from input and return them in a list
def get_nums(line):
    return [int(num) for num in line.split()]

# Exchange nums[n] and nums[m]
def swap(nums, n, m):
    nums[n], nums[m] = nums[m], nums[n]
  
# Print the results of a given sort for a given list of numbers    
def print_results (type, numbers, swaps, comparisons, extra_bytes):
    print (type, "Results")
    print(f'Sorted numbers: {numbers}')
    print(f'Comparisons: {comparisons}')
    print(f'Swaps: {swaps}')
    print(f'Extra Bytes: {extra_bytes}\n')
    

###############  Zybooks Selction Sort
def selection_sort(numbers):
    selectionSortStats = SortStatistics(sortType="Selection Sort", nums=numbers)
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            selectionSortStats.comparisons += 1
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
    
        # Swap numbers[i] and numbers[index_smallest]
        selectionSortStats.swaps += 1
        swap(numbers, i, index_smallest)

    print(selectionSortStats)

###############  Zybooks Insertion Sort
def insertion_sort(numbers):
    insertSortStats = SortStatistics(sortType="Insertion Sort", nums=numbers)

    for i in range(1, len(numbers)):
        j = i
        # Insert numbers[i] into sorted part
        # stopping once numbers[i] is in correct position
        while j > 0:
            insertSortStats.comparisons += 1
            if numbers[j] < numbers[j - 1]:    
                insertSortStats.swaps += 1
                swap(numbers, j, j-1)                               
                j -= 1
            else:
                break                          
    print(insertSortStats)

        
##############  Zybooks Merge Sort        
def merge(numbers, i, j, k, sortStat):

    '''
    global comparisons
    global swaps
    global extra_bytes
    '''

    merged_size = k - i + 1  
    merged_numbers = []
    for l in range(merged_size):
        sortStat.extra_bytes += 4
        merged_numbers.append(0)

    merge_pos = 0                         

    left_pos = i                         
    right_pos = j + 1                   

    while left_pos <= j and right_pos <= k:
        # Added for solution
        sortStat.comparisons += 1
        if numbers[left_pos] < numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos = left_pos + 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1

    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    merge_pos = 0
    while merge_pos < merged_size:
        numbers[i + merge_pos] = merged_numbers[merge_pos]
        merge_pos = merge_pos + 1


def merge_sort(numbers, i, k, sortStat):


    j = 0
    if i < k:
        j = (i + k) // 2 

        merge_sort(numbers, i, j, sortStat)
        merge_sort(numbers, j + 1, k, sortStat)

        merge(numbers, i, j, k, sortStat)

        
############## Zybooks Quick Sort
def partition(numbers, i, k, sortStat):

    #  Pick middle element as pivot 
    midpoint = i + (k - i) // 2
    pivot = numbers[midpoint]

    #  Initialize variables
    done = False
    l = i
    h = k
    while not done:
        #  Increment l while numbers[l] < pivot 
        while numbers[l] < pivot:
            l = l + 1
        #  Decrement h while pivot < numbers[h] 
        while pivot < numbers[h]:
            h = h - 1
        """  If there are zero or one items remaining,
              all numbers are partitioned. Return h """
        sortStat.comparisons += 1
        if l >= h:
            done = True
        else:
            sortStat.swaps += 1
            swap(numbers, l, h)      
            l = l + 1
            h = h - 1
    return h


def quick_sort(numbers, i, k, sortStat):


    j = 0
    """  Base case: If there are one or zero entries to sort,
          partition is already sorted  """ 
    sortStat.comparisons += 1
    if i >= k:
        return
    """  Partition the data within the array. Value j returned
          from partitioning is location of last item in low partition. """ 
    j = partition(numbers, i, k, sortStat)
    """  Recursively sort low partition (i to j) and
          high partition (j + 1 to k) """
    quick_sort(numbers, i, j, sortStat)
    quick_sort(numbers, j + 1, k, sortStat)
    
    return
        

def main():


    # open file
    debug = False
    if debug:
        in_data = open('sort.in')
    else:
        in_data = sys.stdin        
        
    # read each line and analyze, each line is a set of number to sort
    line = in_data.readline()
    while line != "":
        original_nums = get_nums(line)
        print ("########################### New Numbers")
        print(f'##### Original numbers: {original_nums}\n')
        
        # Selection Sort
        nums_to_sort = original_nums.copy()
        selection_sort (nums_to_sort)
        
        # Insertion Sort
        nums_to_sort = original_nums.copy()      
        insertion_sort (nums_to_sort)


        # Merge Sort
        nums_to_sort = original_nums.copy()

        # required here for merge and quick sort only
        MergeSortStats = SortStatistics(sortType="Merge Sort", nums=nums_to_sort)

        merge_sort (nums_to_sort, 0, len(nums_to_sort)-1, MergeSortStats)
        print(MergeSortStats)


        # Quick Sort
        nums_to_sort = original_nums.copy()

        #create sts object here
        quickSortStats = SortStatistics(sortType="Quick Sort", nums=nums_to_sort)

        quick_sort (nums_to_sort, 0, len(nums_to_sort)-1, quickSortStats)
        print(quickSortStats)

        print()
        line = in_data.readline()


if __name__ == "__main__":
    main()