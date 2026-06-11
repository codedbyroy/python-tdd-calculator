# Bug Report

**Jira Issue Key (if applicable):** KAN-XX

## 🐛 Bug Description
Clear and concise description of the bug.

## 🔄 Steps to Reproduce
1. Create a Calculator instance
2. Call `calc.divide(10, 3)`
3. Observe the result

## ✅ Expected Behavior
What should happen when the code runs correctly?

## ❌ Actual Behavior
What actually happens with the bug?

## 💻 Environment
- **Python Version:** 3.9
- **Operating System:** macOS
- **Repository Branch:** main
- **Commit/Version:** (commit hash or branch name)

## 📋 Test Case
```python
from calculator import Calculator

calc = Calculator()
result = calc.divide(10, 3)
print(result)  # Expected: 3.333..., Got: ?
```

## 📝 Error Log/Output
```
Traceback (most recent call last):
  File "...", line X, in <module>
    ...
Exception: ...
```

## 🔍 Additional Context
Any additional context or screenshots that help explain the issue.

## ✅ Checklist
- [ ] I've searched for existing bug reports
- [ ] I'm using the latest version
- [ ] I can reproduce the issue consistently
- [ ] Error message and steps are clear
