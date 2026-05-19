"""
Простой калькулятор для демонстрации публикации пакета.
"""


class Calculator:
    """Класс для выполнения базовых математических операций."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Сложение двух чисел."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Вычитание двух чисел."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Умножение двух чисел."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Деление двух чисел."""
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b


def greet() -> str:
    """Приветственное сообщение."""
    return "Hello from Awesome Calculator v2 by Ratovskiy!"
