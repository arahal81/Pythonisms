from pythonisms.genrator import GLinkedList

def test_print_linked_list():
    ll=GLinkedList()
    ll.insert(2)
    ll.insert(4)
    ll.insert(6)
    ll.insert(8)
    assert "[8] -> [6] -> [4] -> [2] -> None"==ll.__str__()
def test_print_index_linked_list():
    ll=GLinkedList()
    ll.insert(2)
    ll.insert(4)
    ll.insert(6)
    ll.insert(8)
    assert ll[1]==6