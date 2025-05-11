# tests/test_stack.py
import pytest
from src.stack import Stack

@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def filled_stack():
    s = Stack()
    for i in range(5):
        s.push(i)
    return s


class TestStackBasic:
    def test_is_empty_initial(self, empty_stack):
        assert empty_stack.is_empty()

    def test_push_peek(self, empty_stack):
        empty_stack.push(99)
        assert empty_stack.peek() == 99
        assert not empty_stack.is_empty()

    def test_push_pop_fifo(self, empty_stack):
        for i in range(10):
            empty_stack.push(i)
        for i in reversed(range(10)):
            assert empty_stack.pop() == i
        assert empty_stack.is_empty()
    
    def test_pop_empty_raises(self, empty_stack):
        with pytest.raises(IndexError):
            empty_stack.pop()

def test_push_amortized_O1(benchmark):
    s = Stack()
    benchmark(lambda: s.push(0))
