import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):  # позитивный тест умножения
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_failed(self):  # негативный тест умножения
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_correctly(self):  # позитивный тест деления
        assert self.calc.division(self, 10, 5) == 2

    def test_subtraction_calculate_correctly(self):  # позитивный тест вычитания
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_adding_calculate_correctly(self):  # позитивный тест сложения
        assert self.calc.adding(self, 10, 5) == 15

