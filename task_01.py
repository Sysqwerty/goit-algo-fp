class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        print(f"Added to the beginning: {data}")
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        print(f"Added to the end: {data}")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Insert after node
    def insert_after_node(self, prev_node: Node, data):
        print(f"Added {data} after {prev_node.data}")
        if prev_node is None:
            print(f"'{prev_node}' node doesn't exist. Can't insert new node")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Delete
    def delete_node(self, key: int):
        print(f"Deleting: {key}")
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    # Search
    def search_node(self, data: int) -> Node | None:
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    # Reverse
    def reverse_linked_list(self):
        print("Reverse linked list")
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Insertion sort
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next

            # Insert current node into the sorted part of the list
            if sorted_head is None or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

            current = next_node

        # Update the head of the linked list with the sorted part
        self.head = sorted_head

    # Merge sorted lists
    def merge_sorted_lists(self, other_list):
        print(f"Merging current list with provided")
        merged = LinkedList()
        current_self = self.head
        current_other = other_list.head

        while current_self is not None and current_other is not None:
            if current_self.data < current_other.data:
                merged.insert_at_end(current_self.data)
                current_self = current_self.next
            else:
                merged.insert_at_end(current_other.data)
                current_other = current_other.next

        # If one of the lists is not fully traversed, add remaining elements
        while current_self is not None:
            merged.insert_at_end(current_self.data)
            current_self = current_self.next

        while current_other is not None:
            merged.insert_at_end(current_other.data)
            current_other = current_other.next

        return merged

    # Print list
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    # Create a linked list
    llist = LinkedList()

    # Insertion to the beginning
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # List printing
    print("List after insertion at the beginning:")
    llist.print_list()
    print("\n----------------------------------\n")

    # Insertion to the end
    llist.insert_at_end(20)
    llist.insert_at_end(30)

    # List printing
    print("List after insertion at the end:")
    llist.print_list()
    print("\n----------------------------------\n")

    # Insertion after a node
    llist.insert_after_node(llist.head.next, 25)

    # List printing
    print("List after insertion after a node:")
    llist.print_list()
    print("\n----------------------------------\n")

    # Deletion
    llist.delete_node(20)

    # List printing
    print("List after deletion:")
    llist.print_list()
    print("\n----------------------------------\n")

    # Search
    print(
        f"Search for 15: {llist.search_node(15).data if llist.search_node(15) else None}")
    print("\n----------------------------------\n")

    # Reverse
    llist.reverse_linked_list()

    # List printing
    print("List after reverse:")
    llist.print_list()
    print("\n----------------------------------\n")

    # Insertion sort
    print("List after insertion sort:")
    llist.insertion_sort()
    llist.print_list()
    print("\n----------------------------------\n")

    # Merge sorted lists
    print("Creating another list for merging:")
    other_list = LinkedList()
    other_list.insert_at_end(12)
    other_list.insert_at_end(8)
    other_list.insert_at_end(18)
    other_list.insertion_sort()
    print("Other list after sorting:")
    other_list.print_list()
    print("\n----------------------------------\n")
    merged_list = llist.merge_sorted_lists(other_list)
    print("Merged list:")
    merged_list.print_list()
    print("\n----------------------------------\n")
