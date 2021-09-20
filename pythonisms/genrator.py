class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        self._length = 0
        if collection:
            for item in reversed(collection):
                self.insert(item)




class GLinkedList(LinkedList):

    def traverse(self, action):
        current = self.head
        while current:
            action(current.value)
            current = current.next

    def __iter__(self):
        def generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return generator()

    def __str__(self):
        out = ""
        for value in self:
            out += f"[{value}] -> "
        return out + "None"

    def __len__(self):
        return self._length

    def insert(self, value):
        self.head = Node(value, self.head)
        self._length += 1

    def __getitem__(self, index):

        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError


if __name__ == '__main__':
    list = GLinkedList()
    list.insert(2)
    list.insert(4)
    list.insert(6)
    list.insert(8)

    def get_number():

        numbers = [1,2, 4, 6, 8]
        for i in numbers:
            yield i

    # gen = get_number()
    print(list)
    print(f"item at index 2: {list[1]}")
    print(f"length of list: {len(list)}")
    list2 = GLinkedList([1,2,3, 4, 5, 6])
    print(list2)
