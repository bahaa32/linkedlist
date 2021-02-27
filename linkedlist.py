from __future__ import annotations
from typing import Iterator, Optional

class ListNode:
    # TODO: Add option to pass unlimited number of args
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
    def __init__(self):
        self._head: Optional[ListNode] = None
        self._length: int = 0
        self._last_node: Optional[ListNode] = None
        # TODO: add self._cur

    def __delitem__(self, index) -> None:
        # Index beyond list
        if self._length <= index > -1 * self._length:
            raise IndexError
        # Index is first element
        if index == 0:
            if self._head is not None:
                self._head = self._head.next
                self._length -= 1
                return
        # Check if index is negative
        if index < 0:
            index += self._length
        cur = self._head
        for _ in range(0, index - 1):
            cur = cur.next
        cur.next = cur.next.next
        self._length -= 1
        if index == len(self) - 1:
            self._last_node = cur

    def __len__(self) -> int:
        return self._length

    def __setitem__(self, index: int, value) -> None:
        # Index beyond list
        if self._length <= index > -1 * self._length:
            raise IndexError
        # Check if index is negative
        if index < 0:
            index += self._length
        # Index is last element
        if index == self._length - 1:
            self._last_node.val = value
            return
        cur = self._head
        for _ in range(0, index):
            cur = cur.next
        cur.val = value

    def __repr__(self) -> str: # pragma: no cover
        return str({
            "length": self._length,
            "head": self._head
        })

    # TODO: Improve output based on value type
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

    # TODO: DRY
    def __getitem__(self, index: int):
        # Index beyond list
        if index >= self._length:
            raise IndexError
        # Index is first element
        if index == 0:
            return self._head.val
        # Index is last element
        if index == self._length - 1:
            return self._last_node.val
        # Check if index is negative and in possible
        #   range of indeces
        if index < 0 and index > -1 * self._length:
            index += self._length
        cur = self._head
        for _ in range(0, index):
            cur = cur.next
        return cur.val

    def _nodes(self) -> Iterator:
        cur = self._head
        while cur is not None:
            yield cur
            cur = cur.next

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

    # For the commented functions, waiting until I define _find()

    # def index(self, value) -> int:
    #     pass

    # def insert(self, pos: int, value) -> None:
    #     pass

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
