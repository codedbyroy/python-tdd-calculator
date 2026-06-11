"""
Example usage of the calculator in both phases
"""

from calculator import Calculator as SimpleCalculator

print("=" * 60)
print("GREEN PHASE: Simple Calculator Usage")
print("=" * 60)

calc = SimpleCalculator()

# Basic Operations
print("\n--- Basic Operations ---")
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 3 = {calc.subtract(10, 3)}")
print(f"4 × 3 = {calc.multiply(4, 3)}")
print(f"10 ÷ 2 = {calc.divide(10, 2)}")

# Advanced Operations
print("\n--- Advanced Operations ---")
print(f"2^3 = {calc.power(2, 3)}")
print(f"√16 = {calc.square_root(16)}")
print(f"20% of 100 = {calc.percentage(100, 20)}")
print(f"10 mod 3 = {calc.modulo(10, 3)}")

# Memory Operations
print("\n--- Memory Operations ---")
calc.memory_add(5)
calc.memory_add(3)
print(f"Memory recall: {calc.memory_recall()}")
calc.memory_clear()
print(f"After clear: {calc.memory_recall()}")

# History
print("\n--- Operation History ---")
print(f"Total operations: {len(calc.get_history())}")
print("\nLast 3 operations:")
for op in calc.get_history()[-3:]:
    print(f"  {op}")

print("\n" + "=" * 60)

# Now let's test the refactored version
print("\nREFACTOR PHASE: Advanced Calculator Usage")
print("=" * 60)

from calculator_refactored import Calculator as AdvancedCalculator, CalculatorError

calc2 = AdvancedCalculator()

# Basic Operations with same examples
print("\n--- Basic Operations ---")
print(f"5 + 3 = {calc2.add(5, 3)}")
print(f"10 - 3 = {calc2.subtract(10, 3)}")
print(f"4 × 3 = {calc2.multiply(4, 3)}")
print(f"10 ÷ 2 = {calc2.divide(10, 2)}")

# Error Handling
print("\n--- Error Handling ---")
try:
    calc2.divide(10, 0)
except CalculatorError as e:
    print(f"✓ Caught error: {e}")

try:
    calc2.square_root(-4)
except CalculatorError as e:
    print(f"✓ Caught error: {e}")

# History with better methods
print("\n--- Advanced History Features ---")
calc2.add(5, 3)
calc2.multiply(2, 4)
calc2.power(2, 3)
print(f"Last operation: {calc2.get_last_operation()}")
print(f"Total operations: {calc2.get_history_count()}")

print("\n" + "=" * 60)
