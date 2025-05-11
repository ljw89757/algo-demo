# src/stack.py
class Stack:
    """Array-backed stack.

    Operations
    ----------
    push(x)   : O(1) amortized
    pop()     : O(1)
    peek()    : O(1)
    is_empty(): O(1)
    """

    __slots__ = ("_data",)

    def __init__(self) -> None:
        self._data: list[Any] = []


    def push(self, x) -> None:
        self._data.append(x)

    
    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()
    

    def peek(self):
        return self._data[-1]
    

    def is_empty(self) -> bool:
        return not self._data