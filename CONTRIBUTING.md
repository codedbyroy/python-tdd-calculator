# Contribution Guidelines

## Smart Commit References to Jira

When making commits, pull requests, or branch names, reference your Jira issues using the format: `KAN-<number>`

### Commit Message Format

```
<JIRA-KEY> [#<COMMAND>] <message>
```

**Example Commits:**

```bash
# Simple commit
git commit -m "KAN-1 Implement add operation"

# Mark issue as done
git commit -m "KAN-2 #done Implement subtract function"

# Add comment to issue
git commit -m "KAN-3 #comment Fixed edge case with zero"

# Multiple commands
git commit -m "KAN-4 #comment Fixed the bug #inprogress Ready for testing"
```

### Smart Commit Commands

- `#done` / `#close` - Transition issue to Done/Resolved
- `#inprogress` - Move issue to In Progress
- `#review` - Move issue to Review/QA
- `#comment <text>` - Add a comment to the issue
- `#time <hours>` - Log time spent on the issue

### Branch Naming Convention

Use the following pattern:

```
<type>/<JIRA-KEY>-<description>
```

**Types:**
- `feature/` - New feature
- `bugfix/` - Bug fix
- `refactor/` - Code refactoring
- `test/` - Test addition
- `docs/` - Documentation

**Examples:**
```bash
feature/KAN-1-implement-basic-operations
bugfix/KAN-5-fix-division-by-zero
refactor/KAN-8-improve-memory-management
test/KAN-10-add-edge-case-tests
docs/KAN-12-update-api-documentation
```

### Pull Request Format

**Title:**
```
KAN-1 Implement Basic Operations
```

**Description:**
```markdown
## Summary
Implements the basic arithmetic operations (add, subtract, multiply, divide) for the calculator.

## Related Jira Issues
- Implements: KAN-1
- Fixes: KAN-5
- Blocks: KAN-8

## Changes
- Added `add()` method
- Added `subtract()` method
- Added `multiply()` method
- Added `divide()` method with zero-check
- Added 10 comprehensive unit tests

## Testing
```bash
pytest test_calculator.py::TestCalculatorBasicOperations -v
```

## Checklist
- [x] Tests written and passing
- [x] Code reviewed
- [x] Documentation updated
```

### Automatic Jira Updates

When you reference Jira issues in your commits, the following happens automatically:

✅ **Commits linked** to the issue  
✅ **Branches linked** to the issue  
✅ **Pull Requests linked** to the issue  
✅ **Development panel updated** in Jira  
✅ **Issue transitions** (if using smart commit commands)  
✅ **Comments added** (if using `#comment`)  

---

## TDD Development Workflow Example

### Step 1: Create Feature Branch
```bash
git checkout -b feature/KAN-1-basic-operations
```

### Step 2: Write RED Tests
```bash
git commit -m "KAN-1 Write failing tests for add operation"
git commit -m "KAN-1 Write failing tests for subtract operation"
```

### Step 3: Implement GREEN Code
```bash
git commit -m "KAN-1 Implement add and subtract methods"
git commit -m "KAN-1 All tests passing"
```

### Step 4: Refactor
```bash
git commit -m "KAN-1 Refactor with type hints"
git commit -m "KAN-1 #done Refactoring complete"
```

### Step 5: Create Pull Request
```bash
git push origin feature/KAN-1-basic-operations
```

Create a PR with title:
```
KAN-1 Implement Basic Arithmetic Operations
```

### Step 6: Code Review & Merge
Once approved and merged:
```bash
git commit -m "KAN-1 #done Merged to main"
```

---

## Testing Checklist Before Commit

```bash
# Run all tests
pytest test_calculator.py -v

# Run with coverage
pytest test_calculator.py --cov=calculator --cov=calculator_refactored

# Run specific test
pytest test_calculator.py::TestCalculatorBasicOperations -v
```

---

## Common Issue Keys

Refer to your Jira board for issue keys, typically formatted as:
- `KAN-1` through `KAN-N` (based on your Jira project)

---

## Questions?

Refer to:
- [GitHub for Jira Documentation](https://marketplace.atlassian.com/apps/1218383/github-for-jira)
- [Atlassian Smart Commits Guide](https://support.atlassian.com/bitbucket-cloud/docs/use-smart-commits/)
