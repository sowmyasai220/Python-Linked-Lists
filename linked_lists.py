"""
Assignment: User-Defined Linked List Classes
Includes Singly, Doubly, and Circular Linked Lists.

Each list stores arbitrary Python objects (int, str, list, dict, tuple,
custom objects, or other data structures). No type restriction is imposed.
Positions are zero-based.
"""


class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        count, current = 0, self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def insert_beginning(self, data):
        node = SinglyNode(data)
        node.next = self.head
        self.head = node

    def insert_end(self, data):
        node = SinglyNode(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise IndexError("Index out of range")
        if index == 0:
            self.insert_beginning(data)
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        node = SinglyNode(data)
        node.next = current.next
        current.next = node

    def delete_beginning(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        data = self.head.data
        self.head = self.head.next
        return data

    def delete_end(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        if self.head.next is None:
            return self.delete_beginning()
        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        return data

    def delete_at(self, index):
        if index < 0 or index >= self.length():
            raise IndexError("Index out of range")
        if index == 0:
            return self.delete_beginning()
        current = self.head
        for _ in range(index - 1):
            current = current.next
        data = current.next.data
        current.next = current.next.next
        return data

    def search(self, value):
        current, index = self.head, 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def update(self, index, new_data):
        if index < 0:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        current.data = new_data

    def reverse(self):
        previous, current = None, self.head
        while current:
            following = current.next
            current.next = previous
            previous = current
            current = following
        self.head = previous

    def to_list(self):
        result, current = [], self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def display(self):
        print(" -> ".join(repr(item) for item in self.to_list()) + " -> None")

    def clear(self):
        self.head = None

    def __len__(self):
        return self.length()

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        return " -> ".join(repr(item) for item in self.to_list()) + (" -> None" if self.head else "None")


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def length(self):
        count, current = 0, self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def insert_beginning(self, data):
        node = DoublyNode(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_end(self, data):
        node = DoublyNode(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def insert_at(self, index, data):
        size = self.length()
        if index < 0 or index > size:
            raise IndexError("Index out of range")
        if index == 0:
            self.insert_beginning(data)
        elif index == size:
            self.insert_end(data)
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            node = DoublyNode(data)
            node.prev, node.next = current.prev, current
            current.prev.next = node
            current.prev = node

    def delete_beginning(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return data

    def delete_end(self):
        if self.tail is None:
            raise IndexError("Cannot delete from an empty list")
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return data

    def delete_at(self, index):
        size = self.length()
        if index < 0 or index >= size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.delete_beginning()
        if index == size - 1:
            return self.delete_end()
        current = self.head
        for _ in range(index):
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev
        return current.data

    def search(self, value):
        current, index = self.head, 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def update(self, index, new_data):
        if index < 0:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        current.data = new_data

    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def to_list(self):
        result, current = [], self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def to_list_reverse(self):
        result, current = [], self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result

    def display(self):
        print("None <-> " + " <-> ".join(repr(item) for item in self.to_list()) + " <-> None")

    def clear(self):
        self.head = self.tail = None

    def __len__(self):
        return self.length()

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        return " <-> ".join(repr(item) for item in self.to_list()) or "None"


class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def length(self):
        if self.head is None:
            return 0
        count, current = 1, self.head.next
        while current is not self.head:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def insert_beginning(self, data):
        node = CircularNode(data)
        if self.head is None:
            self.head = self.tail = node
            node.next = node
        else:
            node.next = self.head
            self.tail.next = node
            self.head = node

    def insert_end(self, data):
        node = CircularNode(data)
        if self.head is None:
            self.head = self.tail = node
            node.next = node
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node

    def insert_at(self, index, data):
        size = self.length()
        if index < 0 or index > size:
            raise IndexError("Index out of range")
        if index == 0:
            self.insert_beginning(data)
        elif index == size:
            self.insert_end(data)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            node = CircularNode(data)
            node.next = current.next
            current.next = node

    def delete_beginning(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        data = self.head.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return data

    def delete_end(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        if self.head is self.tail:
            return self.delete_beginning()
        current = self.head
        while current.next is not self.tail:
            current = current.next
        data = self.tail.data
        self.tail = current
        self.tail.next = self.head
        return data

    def delete_at(self, index):
        size = self.length()
        if index < 0 or index >= size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.delete_beginning()
        if index == size - 1:
            return self.delete_end()
        current = self.head
        for _ in range(index - 1):
            current = current.next
        data = current.next.data
        current.next = current.next.next
        return data

    def search(self, value):
        if self.head is None:
            return -1
        current, index = self.head, 0
        while True:
            if current.data == value:
                return index
            current = current.next
            index += 1
            if current is self.head:
                return -1

    def update(self, index, new_data):
        size = self.length()
        if index < 0 or index >= size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = new_data

    def reverse(self):
        if self.head is None or self.head is self.tail:
            return
        previous = self.tail
        current = self.head
        original_head = self.head
        while True:
            following = current.next
            current.next = previous
            previous = current
            current = following
            if current is original_head:
                break
        self.tail = original_head
        self.head = previous
        self.tail.next = self.head

    def to_list(self):
        result = []
        if self.head is None:
            return result
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current is self.head:
                break
        return result

    def display(self):
        if self.head is None:
            print("Empty circular linked list")
        else:
            print(" -> ".join(repr(item) for item in self.to_list()) + " -> (back to head)")

    def clear(self):
        self.head = self.tail = None

    def __len__(self):
        return self.length()

    def __iter__(self):
        if self.head is None:
            return
        current = self.head
        while True:
            yield current.data
            current = current.next
            if current is self.head:
                break

    def __str__(self):
        if self.head is None:
            return "Empty circular linked list"
        return " -> ".join(repr(item) for item in self.to_list()) + " -> (back to head)"


if __name__ == "__main__":
    # Demonstration: a list can store different Python data types together.
    sample_values = [10, "hello", [1, 2, 3], {"course": "DSA"}, (4, 5)]

    for list_class in (SinglyLinkedList, DoublyLinkedList, CircularLinkedList):
        linked_list = list_class()
        for value in sample_values:
            linked_list.insert_end(value)
        print(f"\n{list_class.__name__}")
        linked_list.display()
        print("Length:", linked_list.length())
        print("Index of 'hello':", linked_list.search("hello"))
        linked_list.insert_at(2, {"new": "item"})
        print("After insertion:", linked_list)
        linked_list.update(0, "updated")
        print("After update:", linked_list)
        print("Deleted item:", linked_list.delete_at(1))
        linked_list.reverse()
        print("After reverse:", linked_list)
