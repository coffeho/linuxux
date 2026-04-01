import sys
sys.path.append("../src")
from math_demo import (add, add_with_bug, calculate_tax_with_bug, calculate_tax)

def test_addition():
    assert add(2, 2) == 4
    print("Test BASIC ADDITION passed")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    print("Test BASIC ADDITION WITH BUG passed")

def test_addition_duplicated():
    assert add(2, 3) == 2 + 3
    print("Test BASIC ADDITION DUPLICATED passed")

def test_addition_overcomplicated():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == sum([i, j])
            assert add(-i, j) == sum([-i, j])
            assert add(i, -j) == sum([i, -j])
            assert add(-i, -j) == sum([-i, -j])
    print("Test BASIC ADDITION REASONABLE passed")

def test_addition_commutative():
    assert add(-6, 7) == 1
    assert add(7, -6) == 1
    print("Test BASIC ADDITION COMMUTATIVE passed")

def test_tax_calculation_pesticised():
    assert calculate_tax_with_bug(1000) == 150.0
    assert calculate_tax_with_bug(100) == 15.0
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(245) == 36.75
    assert calculate_tax_with_bug(-200) == -30.0
    assert calculate_tax_with_bug(0) == 0.0
    print("Test TAX CALCULATION PESTICIDE passed")

def test_tax_calculation():
    assert calculate_tax(1000) == 150.0
    assert calculate_tax(100) == 15.0
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(245) == 36.75
    assert calculate_tax(-200) == -30.0
    assert calculate_tax(0) == 0.0
    print("Test TAX CALCULATION passed")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
    #test_addition_overcomplicated()
    test_addition_commutative()
    test_tax_calculation()