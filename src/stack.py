"""A linked list implementation of a stack."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class Link(Generic[T]):
    """A link in a linked list."""

    head: T
    tail: List[T]


List = Optional[Link[T]]


class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        self.stack = []

    def push(self, x: T) -> None:
        """Push x on the top of this stack."""
        self.stack.append(x)

    def top(self) -> T:
        """Return the top of the stack."""
        return self.stack[-1]
        
    def pop(self) -> T:
        """Pop the top element off the stack and return it."""
        value = self.stack[-1]
        self.stack.pop()
        return value

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        if not self.stack:
            return False
        else: 
            return True 


stack = Stack()
stack.push(1)
stack.push(4)
stack.push(3)
print(stack.pop())
print(stack.top())