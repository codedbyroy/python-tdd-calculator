# Python TDD Calculator

A Test-Driven Development (TDD) implementation of a Python calculator demonstrating the Red-Green-Refactor cycle.

## Project Structure

### Files

- **`test_calculator.py`** - Test suite with comprehensive test cases (RED PHASE)
- **`calculator.py`** - Basic calculator implementation (GREEN PHASE)
- **`calculator_refactored.py`** - Refactored, production-ready implementation (REFACTOR PHASE)
- **`conftest.py`** - Pytest configuration
- **`requirements.txt`** - Project dependencies
- **`README.md`** - This file
- **`examples.py`** - Usage examples showing both phases

## TDD Phases

### 🔴 RED PHASE: Test-First Development

All tests are written first and intentionally fail:

```bash
pytest test_calculator.py -v
```

Test categories:
1. **Basic Operations**: add, subtract, multiply, divide
2. **Advanced Operations**: power, square_root, percentage, modulo
3. **Memory Functions**: memory_add, memory_recall, memory_clear
4. **History Tracking**: operation history with timestamps

### 🟢 GREEN PHASE: Minimal Implementation

`calculator.py` provides minimal implementation to pass all tests:
- Simple, straightforward implementations
- Focuses on making tests pass
- Includes basic history tracking
- Memory management functionality

### 🟡 REFACTOR PHASE: Clean Code

`calculator_refactored.py` provides production-ready code:
- Well-organized class structure
- Custom data classes and enums
- Comprehensive error handling
- Type hints throughout
- Detailed docstrings
- Separated concerns (Memory, History, Operations)
- Better maintainability and extensibility

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests
pytest test_calculator.py -v

# Run specific test class
pytest test_calculator.py::TestCalculatorBasicOperations -v

# Run with coverage
pytest test_calculator.py --cov=calculator --cov=calculator_refactored

# Run specific test
pytest test_calculator.py::TestCalculatorBasicOperations::test_add_two_positive_numbers -v
```

## Usage Examples

### Using GREEN PHASE (Simple):
```python
from calculator import Calculator

calc = Calculator()

# Basic operations
print(calc.add(5, 3))           # 8
print(calc.subtract(10, 3))     # 7
print(calc.multiply(4, 3))      # 12
print(calc.divide(10, 2))       # 5.0

# Advanced operations
print(calc.power(2, 3))         # 8
print(calc.square_root(16))     # 4.0
print(calc.percentage(100, 20)) # 20.0
print(calc.modulo(10, 3))       # 1

# Memory operations
calc.memory_add(5)
print(calc.memory_recall())     # 5

# History
print(calc.get_history())
```

### Using REFACTOR PHASE (Production):
```python
from calculator_refactored import Calculator, CalculatorError

calc = Calculator()

try:
    result = calc.divide(10, 0)
except CalculatorError as e:
    print(f"Error: {e}")

# Better error handling
calc.add(5, 3)
calc.multiply(4, 2)
print(calc.get_last_operation())
print(f"Total operations: {calc.get_history_count()}")
```

## Features

✅ **Basic Arithmetic**: +, -, ×, ÷  
✅ **Advanced Operations**: Power, Square Root, Percentage, Modulo  
✅ **Memory Management**: Store and recall values  
✅ **Operation History**: Timestamped operation tracking  
✅ **Error Handling**: Division by zero, negative square root  
✅ **Type Hints**: Full type annotations  
✅ **Comprehensive Tests**: 22 test cases  
✅ **Documentation**: Detailed docstrings  

## Test Coverage

- **Basic Operations**: 10 tests
- **Advanced Operations**: 6 tests
- **Memory Functions**: 3 tests
- **History Tracking**: 3 tests
- **Total**: 22 tests

## Learning Objectives

This project demonstrates:

1. **TDD Workflow**: Red → Green → Refactor
2. **Test-First Development**: Write tests before implementation
3. **Incremental Development**: Build features one at a time
4. **Code Refactoring**: Improve code quality without changing behavior
5. **Best Practices**: Type hints, docstrings, error handling
6. **Python Features**: Data classes, enums, type hints, custom exceptions

## Dependencies

- Python 3.8+
- pytest
- pytest-cov (optional, for coverage reports)

---

## 🔗 GitHub ↔ Jira Integration

This repository is connected to the Jira project at: https://tddcalculator.atlassian.net/jira/software/projects/KAN

### Smart Commits & Issue Linking

To link your GitHub commits and PRs to Jira issues, use the following format:

#### Commit Message Format
```bash
git commit -m "KAN-1 Implement basic add operation"
git commit -m "KAN-2 #done Completed green phase tests"
git commit -m "KAN-3 #comment Added comprehensive error handling"
```

#### Commit Message Transitions (Smart Commits)
- `#done` - Mark issue as Done/Resolved
- `#comment` - Add a comment to the issue
- `#inprogress` - Move issue to In Progress
- `#review` - Move issue to Review

#### Branch Naming Convention
```bash
git checkout -b feature/KAN-1-add-operation
git checkout -b bugfix/KAN-5-fix-division-error
git checkout -b refactor/KAN-8-improve-memory-management
```

#### Pull Request Title Format
```
KAN-2: Implement GREEN phase minimal implementation

- Add basic calculator operations
- Write comprehensive tests
- Fix: #KAN-5
```

### What Gets Synced to Jira

When you push commits with Jira issue keys:
- 📝 **Commits** - Git commits linked to the issue
- 🔀 **Pull Requests** - Associated pull requests
- 🌿 **Branches** - Feature/bug branches
- 📊 **Development Panel** - Complete development activity

### Example Workflow

1. **Create a branch** from Jira or GitHub with issue key:
   ```bash
   git checkout -b feature/KAN-1-basic-operations
   ```

2. **Make commits** referencing the Jira key:
   ```bash
   git commit -m "KAN-1 Implement add and subtract functions"
   git commit -m "KAN-1 Add comprehensive unit tests"
   ```

3. **Create a Pull Request** with the issue key:
   ```
   Title: KAN-1 Implement Basic Operations
   Description: Implements add and subtract functions for the calculator
   ```

4. **Merge the PR** - Jira will automatically update the issue with development activity

---

## 🚀 Development Workflow

### Phase 1: RED (Tests First)
```bash
# Create branch
git checkout -b feature/KAN-1-red-phase-tests

# Reference in commit
git commit -m "KAN-1 Write failing tests for basic operations"

# Push and create PR
git push origin feature/KAN-1-red-phase-tests
```

### Phase 2: GREEN (Minimal Implementation)
```bash
# Create branch
git checkout -b feature/KAN-2-green-phase-implementation

# Reference in commit
git commit -m "KAN-2 Implement minimal calculator code to pass tests"

# When done
git commit -m "KAN-2 #done All tests passing"
```

### Phase 3: REFACTOR (Clean Code)
```bash
# Create branch
git checkout -b feature/KAN-3-refactor-phase

# Reference in commit
git commit -m "KAN-3 Refactor calculator with better architecture"
git commit -m "KAN-3 Add data classes and custom exceptions"
git commit -m "KAN-3 #done Refactor complete"
```

---

## Author

Created with TDD methodology for educational purposes.

**Repository**: https://github.com/codedbyroy/python-tdd-calculator  
**Jira Project**: https://tddcalculator.atlassian.net/jira/software/projects/KAN
