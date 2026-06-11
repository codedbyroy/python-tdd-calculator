"""
Test-Driven Development (TDD) Calculator
Red Phase: Write failing tests first
"""

import pytest
from calculator import Calculator


class TestCalculatorBasicOperations:
    """Test basic arithmetic operations"""
    
    def setup_method(self):
        """Setup calculator instance for each test"""
        self.calc = Calculator()
    
    # RED PHASE: These tests should fail initially
    
    def test_add_two_positive_numbers(self):
        """Test adding two positive numbers"""
        result = self.calc.add(5, 3)
        assert result == 8
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        result = self.calc.add(-5, -3)
        assert result == -8
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers"""
        result = self.calc.add(5, -3)
        assert result == 2
    
    def test_subtract_two_positive_numbers(self):
        """Test subtracting two positive numbers"""
        result = self.calc.subtract(10, 3)
        assert result == 7
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        result = self.calc.subtract(-5, -3)
        assert result == -2
    
    def test_multiply_two_positive_numbers(self):
        """Test multiplying two positive numbers"""
        result = self.calc.multiply(4, 3)
        assert result == 12
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        result = self.calc.multiply(5, 0)
        assert result == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        result = self.calc.multiply(-4, -3)
        assert result == 12
    
    def test_divide_two_positive_numbers(self):
        """Test dividing two positive numbers"""
        result = self.calc.divide(10, 2)
        assert result == 5
    
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers"""
        result = self.calc.divide(-10, -2)
        assert result == 5
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)


class TestCalculatorAdvancedOperations:
    """Test advanced operations"""
    
    def setup_method(self):
        """Setup calculator instance for each test"""
        self.calc = Calculator()
    
    def test_power_operation(self):
        """Test power/exponentiation operation"""
        result = self.calc.power(2, 3)
        assert result == 8
    
    def test_power_zero_exponent(self):
        """Test power with zero exponent"""
        result = self.calc.power(5, 0)
        assert result == 1
    
    def test_square_root(self):
        """Test square root operation"""
        result = self.calc.square_root(16)
        assert result == 4
    
    def test_square_root_negative_raises_error(self):
        """Test that square root of negative raises ValueError"""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-4)
    
    def test_percentage(self):
        """Test percentage calculation"""
        result = self.calc.percentage(100, 20)
        assert result == 20
    
    def test_modulo_operation(self):
        """Test modulo operation"""
        result = self.calc.modulo(10, 3)
        assert result == 1


class TestCalculatorMemory:
    """Test calculator memory functions"""
    
    def setup_method(self):
        """Setup calculator instance for each test"""
        self.calc = Calculator()
    
    def test_memory_add(self):
        """Test memory add function"""
        self.calc.memory_add(5)
        assert self.calc.memory_recall() == 5
    
    def test_memory_clear(self):
        """Test memory clear function"""
        self.calc.memory_add(10)
        self.calc.memory_clear()
        assert self.calc.memory_recall() == 0
    
    def test_multiple_memory_adds(self):
        """Test multiple memory additions"""
        self.calc.memory_add(5)
        self.calc.memory_add(3)
        assert self.calc.memory_recall() == 8


class TestCalculatorHistory:
    """Test calculation history tracking"""
    
    def setup_method(self):
        """Setup calculator instance for each test"""
        self.calc = Calculator()
    
    def test_history_tracking(self):
        """Test that calculations are tracked in history"""
        self.calc.add(5, 3)
        self.calc.multiply(2, 4)
        assert len(self.calc.get_history()) == 2
    
    def test_history_clear(self):
        """Test clearing history"""
        self.calc.add(5, 3)
        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0
    
    def test_history_content(self):
        """Test history contains correct operations"""
        self.calc.add(5, 3)
        history = self.calc.get_history()
        assert "add" in history[0].lower() or "5" in history[0]
