'''
Python Code to implement a heap with general comparison function
'''
def crewcomparer(left, right):
    return left.finalcompletiontime < right.finalcompletiontime

def treasurecomparer(left, right):
    if left.arrival_time + left.remainingsize < right.arrival_time + right.remainingsize: return True
    elif left.arrival_time + left.remainingsize == right.arrival_time + right.remainingsize:
        if left.id < right.id: return True
        else: return False
    else: return False
class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        self.arr = init_array
        self.comparator = comparison_function
        # Write your code here
        n = len(init_array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n,i)


    def heapify(self, n, i):
        cur = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.comparator(self.arr[left], self.arr[cur]) is True:
            cur = left
        if right < n and self.comparator(self.arr[right], self.arr[cur]) is True:
            cur = right
        if cur != i:
            self.arr[cur], self.arr[i] = self.arr[i], self.arr[cur]
            self.heapify(n,cur)


        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.arr.append(value)
        where = len(self.arr) - 1
        while where > 0:
            par = (where-1)//2

            if self.comparator(self.arr[where],self.arr[par]):
                self.arr[where],self.arr[par] = self.arr[par],self.arr[where]
                where = par
            else: break


    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        if len(self.arr) == 0:
            return None

        whatwewant= self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()

        if len(self.arr) > 0:
            self.heapify(len(self.arr), 0)

        return whatwewant
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        if len(self.arr) == 0: return None
        else: return self.arr[0]
        # Write your code here
        pass
    
    # You can add more functions if you want to