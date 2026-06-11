"""
Calculator Implementation - GREEN PHASE
Minimal implementation to make tests pass
"""

import math
from datetime import datetime
from typing import List


class Calculator:
    """Basic calculator with arithmetic operations"""
    
    def __init__(self):
        """Initialize calculator with memory and history"""
        self._memory = 0
        self._history: List[str] = []
    
    # Basic Operations
    def add(self, a: float, b: float) -> float:
        """Add two numbers"""
        result = a + b
        self._add_to_history(f"add({a}, {b}) = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers"""
        result = a - b
        self._add_to_history(f"subtract({a}, {b}) = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers"""
        result = a * b
        self._add_to_history(f"multiply({a}, {b}) = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._add_to_history(f"divide({a}, {b}) = {result}")
        return result
    
    # Advanced Operations
    def power(self, base: float, exponent: float) -> float:
        """Calculate power/exponentiation"""
        result = base ** exponent
        self._add_to_history(f"power({base}, {exponent}) = {result}")
        return result
    
    def square_root(self, number: float) -> float:
        """Calculate square root"""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(number)
        self._add_to_history(f"square_root({number}) = {result}")
        return result
    
    def percentage(self, total: float, percent: float) -> float:
        """Calculate percentage of a number"""
        result = (total * percent) / 100
        self._add_to_history(f"percentage({total}, {percent}%) = {result}")
        return result
    
    def modulo(self, a: float, b: float) -> float:
        """Calculate modulo operation"""
        result = a % b
        self._add_to_history(f"modulo({a}, {b}) = {result}")
        return result
    
    # Memory Operations
    def memory_add(self, value: float) -> None:
        """Add value to memory"""
        self._memory += value
        self._add_to_history(f"memory_add({value}), total: {self._memory}")
    
    def memory_recall(self) -> float:
        """Recall value from memory"""
        return self._memory
    
    def memory_clear(self) -> None:
        """Clear memory"""
        self._memory = 0
        self._add_to_history("memory_clear()")
    
    # History Operations
    def _add_to_history(self, operation: str) -> None:
        """Add operation to history"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._history.append(f"[{timestamp}] {operation}")
    
    def get_history(self) -> List[str]:
        """Get calculation history"""
        return self._history.copy()
    
    def clear_history(self) -> None:
        """Clear calculation history"""
        self._history.clear()
        self._add_to_history("history_cleared()")
