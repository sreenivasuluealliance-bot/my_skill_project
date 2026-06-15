## feat: Add basic calculator operations with zero-division protection

### 📋 Summary
Implement core calculator functions (add, subtract, multiply, divide) with proper error handling for division by zero. This provides a foundation for arithmetic operations with input validation.

### 🔄 Changes Made
- Added `add()` function for addition operations
- Added `subtract()` function for subtraction operations
- Added `multiply()` function for multiplication operations
- Added `divide()` function with zero-division error handling
- Implemented validation to raise `ValueError` when attempting to divide by zero

### 🧪 Testing
- [ ] Unit tests pass for all arithmetic operations
- [ ] Verified division by zero raises `ValueError` with appropriate error message
- [ ] Tested with positive, negative, and decimal numbers
- [ ] Confirmed edge cases (e.g., 0 ÷ x = 0, x ÷ 1 = x)

### ⚠️ Breaking Changes
None

### 📝 Notes
- Division operations return float type
- Zero-division check prevents runtime errors in production
- All functions accept numeric inputs (int or float)
