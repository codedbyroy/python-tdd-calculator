# Pull Request Template

Please include the following information in your pull request:

## 🎯 Jira Issue
**Related Jira Key:** KAN-X  
Reference your Jira issue number here (e.g., KAN-1, KAN-5)

## 📝 Summary
Brief description of what this PR does:
- Implements the basic arithmetic operations (add, subtract, multiply, divide)
- Adds comprehensive unit tests
- Updates documentation

## 🔗 Related Issues
- **Implements:** KAN-1
- **Fixes:** KAN-5 (if applicable)
- **Blocks:** KAN-8 (if applicable)
- **Duplicates:** (if applicable)

## ✅ Changes Made
- Added `add()` method to Calculator class
- Added `subtract()` method to Calculator class
- Added `multiply()` method to Calculator class
- Added `divide()` method with zero-check error handling
- Added 10 comprehensive unit tests in `test_calculator.py`
- Updated README.md with usage examples

## 🧪 Testing

```bash
# Run all tests
pytest test_calculator.py -v

# Run specific test class
pytest test_calculator.py::TestCalculatorBasicOperations -v

# Run with coverage
pytest test_calculator.py --cov=calculator --cov=calculator_refactored
```

**Test Results:**
- [x] All tests passing
- [x] No new warnings
- [x] Coverage meets requirements

## 📋 Checklist
- [ ] Tests written and passing
- [ ] Code follows project style guidelines
- [ ] Documentation updated
- [ ] Related Jira issues referenced
- [ ] No new warnings generated
- [ ] Code review completed
- [ ] Jira issue linked in title/description

## 🔍 How Has This Been Tested?

Describe the tests you ran and how to reproduce:

1. Created new test file
2. Ran pytest with verbose output
3. Verified all 22 tests pass
4. Checked coverage report

## 📸 Screenshots/Output (if applicable)

```bash
$ pytest test_calculator.py -v
================================= test session starts =================================
collected 22 items

test_calculator.py::TestCalculatorBasicOperations::test_add_two_positive_numbers PASSED
test_calculator.py::TestCalculatorBasicOperations::test_subtract_two_positive_numbers PASSED
...

================================= 22 passed in 0.23s =================================
```

## 📝 Additional Notes

Any additional context, questions, or notes for reviewers:

---

## Smart Commit Commands

After this PR is merged, use this commit message to update Jira:
```bash
git commit -m "KAN-X #done Merged to main"
```

This will automatically:
- Mark the issue as Done in Jira
- Link the commit to the issue
- Update the Development panel in Jira
