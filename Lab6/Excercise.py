class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Appends a new node with the specified data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Displays the elements of the list in a readable format."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        """Inserts a new node with the specified data at the given position."""
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        """Deletes the first node with the specified data."""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        """Searches for a node with the specified data and returns its position, or -1 if not found."""
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        """Reverses the linked list in place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        """Finds and returns the middle element's data in the list."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        """Detects if the linked list contains a cycle."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        """Removes duplicate elements from an unsorted linked list."""
        if not self.head:
            return
        seen = set()
        current = self.head
        seen.add(current.data)
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next

    def merge_sorted(self, other):
        """Merges this sorted linked list with another sorted linked list."""
        dummy = Node(0)
        tail = dummy
        a, b = self.head, other.head
        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a if a else b

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

# Test the LinkedList methods
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Middle element:", ll.find_middle())  # Output: 3

ll.append(3)
ll.append(2)
print("Before removing duplicates:")
ll.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 3 -> 2
ll.remove_duplicates()
print("After removing duplicates:")
ll.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5

# Create a cycle for testing
ll.head.next.next.next.next.next = ll.head.next.next  # Creating a cycle
print("Has cycle:", ll.has_cycle())  # Output: True

# Merging two sorted linked lists
ll2 = LinkedList()
ll2.append(1)
ll2.append(3)
ll2.append(5)

ll3 = LinkedList()
ll3.append(2)
ll3.append(4)
ll3.append(6)

merged_list = ll2.merge_sorted(ll3)
print("Merged sorted list:")
merged_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
