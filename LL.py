class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Delete from beginning
    def delete_begin(self):
        if self.head is None:
            return

        # Single node
        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if self.head is None:
            return

        if self.head.next == self.head:
            self.head = None
            return

        prev = None
        curr = self.head

        while curr.next != self.head:
            prev = curr
            curr = curr.next

        prev.next = self.head

    # Search
    def search(self, key):
        if self.head is None:
            return False

        temp = self.head

        while True:
            if temp.data == key:
                return True

            temp = temp.next

            if temp == self.head:
                break

        return False

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.head:
                break


cll = CircularLinkedList()

cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)

cll.display()
# 10 -> 20 -> 30 -> (head)

