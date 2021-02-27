import pytest
from linkedlist import LinkedList, ListNode

# new_ll = LinkedList()
# new_ll.append("Hello, world1!")
# new_ll.append("Hello, world2!")
# new_ll.append("Hello, world3!")
# print(new_ll)
# del new_ll[2]
# print(str(new_ll))

def test_create_list():
    assert isinstance(LinkedList(), LinkedList)

def test_append_and_check():
    new_ll = LinkedList()
    new_ll.append("Hello, world1!")
    new_ll.append("Hello, world2!")
    new_ll.append("Hello, world3!")
    assert len(new_ll) == 3
    assert new_ll[0] == "Hello, world1!"
    assert new_ll[1] == "Hello, world2!"
    assert new_ll[2] == "Hello, world3!"

def test_delete():
    new_ll = LinkedList()
    new_ll.append("Hello, world1!")
    new_ll.append("Hello, world2!")
    new_ll.append("Hello, world3!")
    del new_ll[1]
    assert len(new_ll) == 2
    assert new_ll.pop() == "Hello, world3!"
    assert new_ll[0] == "Hello, world1!"
    assert len(new_ll) == 1
    with pytest.raises(IndexError):
        del new_ll[5]
    new_ll.append("Hello, world2!")
    del new_ll[0]
    assert new_ll[0] == "Hello, world2!"


def test_set():
    new_ll = LinkedList()
    new_ll.append("Hello, world1!")
    new_ll.append("Hello, world2!")
    new_ll.append("Hello, world3!")
    new_ll[1] = 123
    assert len(new_ll) == 3
    assert new_ll[0] == "Hello, world1!"
    assert new_ll[1] == 123
    assert new_ll[2] == "Hello, world3!"
    with pytest.raises(IndexError):
        new_ll[5] = 21
    new_ll[-1] = "Testing 123"
    assert new_ll[2] == "Testing 123"

def test_iterator():
    new_ll = LinkedList()
    new_ll.append("Hello, world1!")
    new_ll.append("Hello, world2!")
    new_ll.append("Hello, world3!")
    iterator = new_ll.__iter__()
    assert next(iterator) == "Hello, world1!"
    assert next(iterator) == "Hello, world2!"
    assert next(iterator) == "Hello, world3!"

def test_nodes():
    new_ll = LinkedList()
    new_ll.append("Hello, world1!")
    new_ll.append("Hello, world2!")
    new_ll.append("Hello, world3!")
    iterator = new_ll._nodes()
    assert next(iterator).val == "Hello, world1!"
    assert next(iterator).val == "Hello, world2!"
    assert next(iterator).val == "Hello, world3!"

def test_clear():
    new_ll = LinkedList()
    new_ll.append("Hello, world1!")
    new_ll.append("Hello, world2!")
    new_ll.append("Hello, world3!")
    new_ll.clear()
    assert len(new_ll) == 0
    with pytest.raises(IndexError):
        new_ll[0]

def test_copy():
    new_ll = LinkedList()
    new_ll.append("Hello, world1!")
    new_ll.append("Hello, world2!")
    new_ll.append("Hello, world3!")
    clone_ll = new_ll.copy()
    clone_nodes = clone_ll._nodes()
    for node in new_ll._nodes():
        assert id(node) != id(next(clone_nodes))

def test_reverse_odd():
    new_ll = LinkedList()
    new_ll.append(4)
    new_ll.append(1)
    new_ll.append(2)
    new_ll.reverse()
    assert new_ll[0] == 2
    assert new_ll[1] == 1
    assert new_ll[2] == 4

def test_reverse_even():
    new_ll = LinkedList()
    new_ll.append(4)
    new_ll.append(1)
    new_ll.append(2)
    new_ll.append(9)
    new_ll.reverse()
    assert new_ll[0] == 9
    assert new_ll[1] == 2
    assert new_ll[2] == 1
    assert new_ll[3] == 4

def test_reverse_empty():
    new_ll = LinkedList()
    new_ll.reverse()
    assert str(new_ll) == "LinkedList()"

def test_reverse_one():
    new_ll = LinkedList()
    new_ll.append(1)
    new_ll.reverse()
    assert str(new_ll) == "LinkedList(int(1))"

def test_sort():
    new_ll = LinkedList()
    new_ll.append(4)
    new_ll.append(1)
    new_ll.append(2)
    new_ll.append(9)
    new_ll.sort()
    assert new_ll[0] == 1
    assert new_ll[1] == 2
    assert new_ll[2] == 4
    assert new_ll[3] == 9

def test_count():
    new_ll = LinkedList()
    new_ll.append(4)
    new_ll.append(1)
    new_ll.append(1)
    new_ll.append(2)
    new_ll.append(2)
    new_ll.append(2)
    new_ll.append(9)
    new_ll.sort()
    assert new_ll.count(4) == 1
    assert new_ll.count(9) == 1
    assert new_ll.count(1) == 2
    assert new_ll.count(2) == 3

def test_extend():
    new_ll = LinkedList()
    new_ll.append(4)
    new_ll.append(1)
    new_ll.extend([4,5])
    for idx, num in enumerate([4,1,4,5]):
        assert new_ll[idx] == num

def test_remove():
    new_ll = LinkedList()
    new_ll.append(4)
    new_ll.append(1)
    new_ll.append(2)
    new_ll.append(7)
    new_ll.append(2)
    new_ll.remove(2)
    new_ll.remove(4)
    for idx, num in enumerate([1,7,2]):
        assert new_ll[idx] == num

def test_eq_node():
    assert ListNode(3) == 3
    assert ListNode(3) == ListNode(3)
    assert ListNode(3) != 2
    assert ListNode(3) != ListNode(2)

@pytest.mark.skip(reason="subject to change")
def test_repr():
    new_ll = LinkedList()
    new_ll.__repr__()
    new_ll.__str__()