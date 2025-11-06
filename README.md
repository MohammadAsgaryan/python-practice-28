# Logging Decorator in Python

This project showcases an advanced use of **decorators** in Python to automatically log function activity into a file.

## ✅ What This Decorator Does
The custom `logger` decorator:
- Records function name
- Logs input arguments
- Saves the return value
- Measures execution time
- Stores everything in `log.txt`

This pattern is commonly used in real-world applications for:
✔ Debugging  
✔ Performance monitoring  
✔ Tracking usage history  
✔ Logging errors or function behavior

---

### ✅ Example Usage
Two functions are decorated:
- `multiply(a, b)` → returns multiplication result after delay
- `hello(name)` → prints a greeting

Each call creates a log entry like:

---

### ✅ How to Run
```bash
python practice.py
