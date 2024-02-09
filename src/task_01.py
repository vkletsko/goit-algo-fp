class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

    def insert(self, new_node):
        if not self.head:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def sorted_insert(self, new_node):
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next and current_node.next.data < new_node.data:
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def merge_sorted_lists(self, list2):
        merged_list = LinkedList()
        current1 = self.head
        current2 = list2.head

        while current1 and current2:
            if current1.data <= current2.data:
                merged_list.sorted_insert(Node(current1.data))
                current1 = current1.next
            else:
                merged_list.sorted_insert(Node(current2.data))
                current2 = current2.next

        while current1:
            merged_list.sorted_insert(Node(current1.data))
            current1 = current1.next

        while current2:
            merged_list.sorted_insert(Node(current2.data))
            current2 = current2.next

        return merged_list

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    # Cортування вставками
    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            sorted_head = self.insertion_sorted_insert(
                sorted_head, current_node)
            current_node = next_node

        self.head = sorted_head

    def insertion_sorted_insert(self, sorted_head, new_node):
        if not sorted_head or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        current_node = sorted_head
        while current_node.next and current_node.next.data < new_node.data:
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
        return sorted_head


if __name__ == "__main__":
    # Створення першого відсортованного списку
    linked_list = LinkedList()
    linked_list.sorted_insert(Node(5))
    linked_list.sorted_insert(Node(3))
    linked_list.sorted_insert(Node(9))
    linked_list.sorted_insert(Node(2))

    print("Перший відсортований список:")
    linked_list.display()

    # Реверсування першого списку
    linked_list.reverse()
    print("Перший список після реверсування:")
    linked_list.display()

    # Створення другого відсортованного списку
    linked_list2 = LinkedList()
    linked_list2.sorted_insert(Node(7))
    linked_list2.sorted_insert(Node(4))
    linked_list2.sorted_insert(Node(8))
    linked_list2.sorted_insert(Node(1))
    linked_list2.sorted_insert(Node(6))

    print("Другий відсортований список:")
    linked_list2.display()

    # Об'єднання відсортованих списків
    merged_list = linked_list.merge_sorted_lists(linked_list2)
    print("Після об'єднання двох відсортованих списків в один відсортований:")
    merged_list.display()

    # Створення другого відсортованного списку
    linked_list3 = LinkedList()
    linked_list3.insert(Node(7))
    linked_list3.insert(Node(4))
    linked_list3.insert(Node(8))
    linked_list3.insert(Node(1))
    linked_list3.insert(Node(6))

    print("Третій не відсортований список:")
    linked_list3.display()

    linked_list3.insertion_sort()
    print("Ітоговий список після сортовання вставками:")
    linked_list3.display()
