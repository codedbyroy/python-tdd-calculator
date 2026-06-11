# Feature Request

**Jira Issue Key (if applicable):** KAN-XX

## ✨ Feature Description
Clear description of the feature you'd like to see implemented.

Example: Add support for logarithm calculations (log base 10, natural log, log base N)

## 🎯 Use Case
Why would this feature be useful? What problem does it solve?

Example: Users need logarithmic calculations for scientific and financial applications.

## 💡 Proposed Implementation
(Optional) How should this feature be implemented?

```python
def log(self, number: float, base: float = 10) -> float:
    """Calculate logarithm of a number"""
    if number <= 0:
        raise ValueError("Cannot calculate log of non-positive number")
    return math.log(number, base)
```

## 🔗 Related Issues
- Related to: KAN-X
- Duplicates: (if applicable)
- Blocked by: (if applicable)

## 📝 Additional Context
Any additional information that helps explain this feature request.

## 🏷️ Category
- [ ] Basic Operations
- [ ] Advanced Operations
- [ ] Memory Management
- [ ] History Tracking
- [ ] Error Handling
- [ ] Documentation
- [ ] Performance
- [ ] Other

## ✅ Checklist
- [ ] Feature is not already implemented
- [ ] Clear use case and benefit
- [ ] Implementation approach considered
- [ ] Tests considered
