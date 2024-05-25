# Implement the following functions for a singly linked list:
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

# Inserts an element at the specified index.

    def insertAt(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

# Deletes the element at the specified index 

    def deleteAt(self, index):
        if index < 0:
            raise IndexError("Index out of bounds")
        if self.head is None:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of bounds")
            current = current.next
        current.next = current.next.next

#Returns the size of the linked list

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
#Returns true if the linked list is empty, false otherwise

    def is_empty(self):
        return self.head is None

#Rotates the linked list by k positions to the right

    def rotate_right(self, k):
        if not self.head or k == 0:
            return
        length = self.size()
        k = k % length
        if k == 0:
            return
        slow, fast = self.head, self.head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = self.head
        self.head = new_head

#Reverses the linked list

    def reverse(self):
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

#Appends an element to the end of the linked list

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

#Prepends an element to the beginning of the linked list

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

#o Merges two linked lists into a single linked list

    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = other_list.head

#Returns the middle element of the linked list

    def get_middle(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

# Returns the index of the first occurrence of the specified element in the linked list, 
#or -1 if the element is not found.

    def index_of(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

#Remaining I not wrote questions that I don't know
#->Splits the linked list into two linked lists at the specified index
#->Interleaves two linked lists into a single linked list