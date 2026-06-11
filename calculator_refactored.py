"""
Calculator Implementation - REFACTOR PHASE
Cleaned up, well-organized, feature-rich implementation
"""

import math
from datetime import datetime
from typing import List, Union
from dataclasses import dataclass
from enum import Enum


class OperationType(Enum):
    """Enum for operation types"""
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
    POWER = "power"
    SQUARE_ROOT = "square_root"
    PERCENTAGE = "percentage"
    MODULO = "modulo"
    MEMORY_ADD = "memory_add"
    MEMORY_CLEAR = "memory_clear"


@dataclass
class Operation:
    """Data class representing a calculator operation"""
    operation_type: OperationType
    operands: List[Union[int, float]]
    result: Union[int, float]
    timestamp: str
    
    def __str__(self) -> str:
        """String representation of operation"""
        return f"[{self.timestamp}] {self.operation_type.value}{self.operands} = {self.result}"


class CalculatorError(Exception):
    """Custom exception for calculator errors"""
    pass


class CalculatorMemory:
    """Manages calculator memory operations"""
    
    def __init__(self):
        """Initialize memory"""
        self._value = 0
    
    def add(self, value: Union[int, float]) -> None:
        """Add to memory"""
        self._value += value
    
    def recall(self) -> Union[int, float]:
        """Recall memory value"""
        return self._value
    
    def clear(self) -> None:
        """Clear memory"""
        self._value = 0


class CalculatorHistory:
    """Manages calculator operation history"""
    
    def __init__(self):
        """Initialize history"""
        self._operations: List[Operation] = []
    
    def add_operation(self, operation: Operation) -> None:
        """Add operation to history"""
        self._operations.append(operation)
    
    def get_all(self) -> List[Operation]:
        """Get all operations"""
        return self._operations.copy()
    
    def get_last(self, count: int = 1) -> List[Operation]:
        """Get last N operations"""
        return self._operations[-count:]
    
    def clear(self) -> None:
        """Clear history"""
        self._operations.clear()
    
    def __len__(self) -> int:
        """Return number of operations in history"""
        return len(self._operations)


class Calculator:
    """
    Advanced calculator with arithmetic operations, memory, and history tracking.
    
    Features:
    - Basic operations: add, subtract, multiply, divide
    - Advanced operations: power, square_root, percentage, modulo
    - Memory management: add, recall, clear
    - Operation history tracking with timestamps
    - Error handling for invalid operations
    """
    
    def __init__(self):
        """Initialize calculator"""
        self._memory = CalculatorMemory()
        self._history = CalculatorHistory()
    
    # ===== BASIC OPERATIONS =====
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Sum of a and b
        """
        result = a + b
        self._record_operation(OperationType.ADD, [a, b], result)
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Subtract two numbers.
        
        Args:
            a: First number
            b: Second number (to be subtracted)
        
        Returns:
            Difference of a and b
        """
        result = a - b
        self._record_operation(OperationType.SUBTRACT, [a, b], result)
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Product of a and b
        """
        result = a * b
        self._record_operation(OperationType.MULTIPLY, [a, b], result)
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Divide two numbers.
        
        Args:
            a: Dividend
            b: Divisor
        
        Returns:
            Quotient of a divided by b
        
        Raises:
            CalculatorError: If attempting to divide by zero
        """
        if b == 0:
            raise CalculatorError("Cannot divide by zero")
        result = a / b
        self._record_operation(OperationType.DIVIDE, [a, b], result)
        return result
    
    # ===== ADVANCED OPERATIONS =====
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """
        Calculate base raised to the power of exponent.
        
        Args:
            base: Base number
            exponent: Exponent
        
        Returns:
            Result of base^exponent
        """
        result = base ** exponent
        self._record_operation(OperationType.POWER, [base, exponent], result)
        return result
    
    def square_root(self, number: Union[int, float]) -> float:
        """
        Calculate square root of a number.
        
        Args:
            number: Number to calculate square root
        
        Returns:
            Square root of number
        
        Raises:
            CalculatorError: If number is negative
        """
        if number < 0:
            raise CalculatorError("Cannot calculate square root of negative number")
        result = math.sqrt(number)
        self._record_operation(OperationType.SQUARE_ROOT, [number], result)
        return result
    
    def percentage(self, total: Union[int, float], percent: Union[int, float]) -> float:
        """
        Calculate percentage of a number.
        
        Args:
            total: Total value
            percent: Percentage value
        
        Returns:
            Calculated percentage
        """
        result = (total * percent) / 100
        self._record_operation(OperationType.PERCENTAGE, [total, percent], result)
        return result
    
    def modulo(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Calculate modulo operation.
        
        Args:
            a: First number
            b: Second number (divisor)
        
        Returns:
            Remainder of a divided by b
        
        Raises:
            CalculatorError: If b is zero
        """
        if b == 0:
            raise CalculatorError("Cannot perform modulo with zero divisor")
        result = a % b
        self._record_operation(OperationType.MODULO, [a, b], result)
        return result
    
    # ===== MEMORY OPERATIONS =====
    
    def memory_add(self, value: Union[int, float]) -> None:
        """Add value to memory"""
        self._memory.add(value)
        self._record_operation(OperationType.MEMORY_ADD, [value], self._memory.recall())
    
    def memory_recall(self) -> Union[int, float]:
        """Recall value from memory"""
        return self._memory.recall()
    
    def memory_clear(self) -> None:
        """Clear memory"""
        self._memory.clear()
        self._record_operation(OperationType.MEMORY_CLEAR, [], 0)
    
    # ===== HISTORY OPERATIONS =====
    
    def get_history(self) -> List[str]:
        """
        Get operation history.
        
        Returns:
            List of operation strings
        """
        return [str(op) for op in self._history.get_all()]
    
    def get_last_operation(self) -> Union[str, None]:
        """
        Get the last operation.
        
        Returns:
            Last operation string or None if history is empty
        """
        last_ops = self._history.get_last(1)
        return str(last_ops[0]) if last_ops else None
    
    def clear_history(self) -> None:
        """Clear operation history"""
        self._history.clear()
    
    def get_history_count(self) -> int:
        """Get number of operations in history"""
        return len(self._history)
    
    # ===== PRIVATE METHODS =====
    
    def _record_operation(
        self,
        operation_type: OperationType,
        operands: List[Union[int, float]],
        result: Union[int, float]
    ) -> None:
        """
        Record operation in history.
        
        Args:
            operation_type: Type of operation
            operands: Operation operands
            result: Operation result
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        operation = Operation(operation_type, operands, result, timestamp)
        self._history.add_operation(operation)
