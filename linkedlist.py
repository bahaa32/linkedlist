from typing import Optional

class ListNode:
    # TODO: Add option to pass unlimited number of args
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return self.val

class LinkedList:
    def __init__(self):
        self._head: Optional[ListNode] = None
        self._length: int = 0
        self._last_node: Optional[ListNode] = None

    def __eq__(self, other_node: ListNode) -> bool:
        return self.val == other_node.val

    def __delattr__(self, val) -> None:
        # First node should be deleted
        if self[0].val == val:
            self[0] = self[0].next
            self._length -= 1
        for node in len(self):
            if node.next == val:
                # Bypass second node and point directly to third node.
                #   This removes all references from LinkedList to the
                #   node and it is garbage collected.
                node.next = node.next.next
                self._length -= 1

    def __sizeof__(self) -> int:
        return self._length

    def append(self, val):
        new_node = ListNode(val)
        if self._head is None:
            self._head = new_node
        else:
            self._last_node.next = new_node
        self._last_node = new_node
        self._length += 1

    def __setattr__(self, index: int, value) -> None:
        # Index beyond list
        if index >= self._length:
            raise IndexError
        # Index is last element
        if index == self._length - 1:
            self._last_node.val = value
            return
        # Check if index is negative and in possible
        #   range of indeces
        if index < 0 and index > -1 * self._length:
            index += self._length
        cur = self._head
        for _ in range(0, index):
            cur = cur.next
        cur.val = value

    def __repr__(self):
        return {
            "length": self._length,
            "head": self._head
        }

    def __str__(self):
        if self._length == 0:
            return "LinkedList()"
        text = "LinkedList("
        for val in self.values():
            text += str(val) + ", "
        return text[:-2] + ")"
