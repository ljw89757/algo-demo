from src.fizzbuzz import fizzbuzz

def test_3():
    assert fizzbuzz(3) == "Fizz"

def test_5():
    assert fizzbuzz(5) == "Buzz"

def test_15():
    assert fizzbuzz(15) == "FizzBuzz"
