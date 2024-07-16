#linkedlist implementation insert,delete,find

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None
ll.delete(2)
ll.print_list()  # Output: 1 -> 3 -> None
print(ll.find(3))  # Output: True
print(ll.find(2))  # Output: False
