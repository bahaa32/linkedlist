from __future__ import annotations
from typing import Iterator, Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next: Optional[ListNode] = None

    def __eq__(self, other) -> bool:
        if isinstance(other, ListNode):
            return self.val == other.val
        return self.val == other


    def __repr__(self) -> str: # pragma: no cover
        return f"ListNode({type(self.val).__name__}({self.val}))"

    def __str__(self) -> str: # pragma: no cover
        return self.val

class LinkedList:
    def __init__(self, iterator: Optional[Iterator] = None):
        self._head: Optional[ListNode] = None
        self._length: int = 0
        self._last_node: Optional[ListNode] = None
        self._cur =[0, None]
        if iterator is not None:
            self.extend(iterator)

    def __delitem__(self, index) -> None:
        cur = self._node_at(index-1)
        if index == 0:
            self._head = self._head.next
            if self._cur[0] == 0:
                self._cur = [0, self._head]
        else:
            cur.next = cur.next.next
            self._length -= 1
            if index == len(self) - 1:
                self._last_node = cur

    def __len__(self) -> int:
        return self._length

    def __setitem__(self, index: int, value) -> None:
        self._node_at(index).val = value

    def __repr__(self) -> str: # pragma: no cover
        return str({
            "length": self._length,
            "head": self._head
        })

    def __str__(self) -> str: # pragma: no cover
        if self._length == 0:
            return "LinkedList()"
        text = "LinkedList("
        for val in self:
            text += f"{type(val).__name__}({str(val)}), "
        return text[:-2] + ")"

    def __iter__(self) -> Iterator:
        cur = self._head
        while cur is not None:
            yield cur.val
            cur = cur.next

    def __getitem__(self, index: int):
        node = self._node_at(index)
        if node is not None:
            return node.val
        else:
            raise IndexError

    def _nodes(self) -> Iterator:
        cur = self._head
        while cur is not None:
            yield cur
            cur = cur.next

    # Inspired by llist
    def _node_at(self, index: int) -> ListNode:
        # Index beyond list
        if self._length <= index > -1 * self._length:
            raise IndexError
        # Index is first element
        if index == 0:
            return self._head
        # Index is last element
        if index == self._length - 1:
            return self._last_node
        # Check if index is negative and in possible
        #   range of indeces
        if index < 0:
            index += self._length
        if self._cur[0] == index:
            return self._cur[1]
        if self._cur[0] < index and self._cur[1] is not None:
            cur = self._cur[1]
            for _ in range(self._cur[0], index):
                cur = cur.next
        else:
            cur = self._head
            for _ in range(0, index):
                cur = cur.next
            self._cur = [index, cur]
        return cur

    def append(self, val) -> None:
        new_node = ListNode(val)
        if self._head is None:
            self._head = new_node
        else:
            self._last_node.next = new_node
        self._last_node = new_node
        self._length += 1

    def clear(self) -> None:
        self._head = None
        self._length = 0
        self._cur = [0, None]

    def copy(self) -> LinkedList:
        new_list = LinkedList()
        for val in self:
            new_list.append(val)
        return new_list

    def count(self, value) -> int:
        counter = 0
        for val in self:
            if val == value:
                counter += 1
        return counter

    def extend(self, iterable) -> None:
        for val in iterable:
            self.append(val)

    def index(self, value) -> int:
        for idx, val in enumerate(self):
            if val == value:
                return idx

    def insert(self, pos: int, value) -> None:
        new_node = ListNode(value)
        if pos == 0:
            new_node.next = self._head
            self._head = new_node
            self._cur[0] += 1
            self._length += 1
            return
        cur = self._node_at(pos)
        if id(cur) == id(self._last_node):
            new_node.next = self._last_node
        new_node.next = cur.next
        cur.next = new_node
        self._length += 1

    def pop(self, index: Optional[int] = -1):
        value = self[index]
        del self[index]
        return value

    def remove(self, val) -> None:
        # First node should be deleted
        if self[0] == val:
            self._head = self._head.next
            self._length -= 1
            return
        for node in self._nodes():
            if node.next == val:
                # Bypass second node and point directly to third node.
                #   This removes all references from LinkedList to the
                #   node and it is garbage collected.
                node.next = node.next.next
                self._length -= 1
                return

    # https://www.geeksforgeeks.org/reverse-a-linked-list/
    # Thanks for the great explainer!
    def reverse(self):
        prev = None
        cur = self._head
        for _ in range(len(self)):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self._last_node, self._head = self._head, self._last_node

    # Bubble sort is possible here but possibly not as fast.
    def sort(self) -> None:
        # Could be faster than list(self) because length is known
        new_array = len(self) * [None]
        for idx, val in enumerate(self):
            new_array[idx] = val
        # Let python sort it better than we can
        new_array.sort()
        cur = self._head
        for val in new_array:
            cur.val = val
            cur = cur.next
