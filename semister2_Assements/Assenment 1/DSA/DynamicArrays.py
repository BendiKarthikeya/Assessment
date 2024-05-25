#Implement the following methods for a dynamic array:

class Dynamicarray:
    def __init__(self, resize=2):
        self.arr = []
        self.size = 0
        self.resize = resize

#Resizing the arrays with custom factor given by user 

    def _resize(self, new_capacity):
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

#Inserts an element at the specified index

    def insertAtIndex(self, index, value):
        if self.size == len(self.arr):
            self._resize(max(1, len(self.arr) * self.resize))
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[index] = value
        self.size += 1

#Deletes the element at the specified index

    def deleteAtIndex(self, index):
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        self.size -= 1
        self.arr[self.size] = None
        if self.size <= len(self.arr) // (self.resize * 2):
            self._resize(max(1, len(self.arr) // self.resize))

# Returns the size of the dynamic array.
    def get_size(self):
        return self.size
    
#Returns true if the dynamic array is empty, false otherwise

    def is_empty(self):
        return self.size == 0

#Rotates the dynamic array by k positions to the right.

    def rotate_right(self, k):
        if self.size == 0 or k == 0:
            return
        k = k % self.size
        self.arr = self.arr[-k:] + self.arr[:-k]

#Reverses the dynamic array.

    def reverse(self):
        left, right = 0, self.size - 1
        while left < right:
            self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
            left += 1
            right -= 1

#Appends an element to the end of the dynamic array

    def append(self, value):
        if self.size == len(self.arr):
            self._resize(max(1, len(self.arr) * self.resize))
        self.arr[self.size] = value
        self.size += 1

#Prepends an element to the beginning of the dynamic array.

    def prepend(self, value):
        self.insert_at_index(0, value)

#Merges two dynamic arrays into a single dynamic array.

    def merge(self, other):
        for element in other.arr[:other.size]:
            self.append(element)

#Returns the middle element of the dynamic array.

    def get_middle(self):
        if self.size == 0:
            return None
        return self.arr[self.size // 2]

#Returns the index of the first occurrence of the specified element in the dynamic 
#array, or -1 if the element is not found.

    def index_of(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                return i
        return -1


#Remaining I not wrote questions that I don't know
#->Interleaves two dynamic arrays into a single dynamic array
#-> Splits the dynamic array into two dynamic arrays at the specified index.
#->Resizing the arrays with custom factor given by user (other than 2)