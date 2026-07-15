# Find Array Dimensions Using `ndim`

## 📖 Overview

This program demonstrates how to determine the number of dimensions of a NumPy array using the `.ndim` attribute.

---

## 📌 Concepts Covered

- One-Dimensional Array (1D)
- Two-Dimensional Array (2D)
- Three-Dimensional Array (3D)
- `.ndim` Attribute

---

## 📚 Syntax

```python
array.ndim
```

The `.ndim` attribute returns the total number of dimensions (axes) of a NumPy array.

---

## 💻 Example

```python
import numpy as np

array = np.array([[1, 2], [3, 4]])

print(array.ndim)
```

Output

```
2
```

---

## 🎯 Output

```
1D Array Dimension: 1
2D Array Dimension: 2
3D Array Dimension: 3
```

---
# Array Attributes

## Programs Included

- find_array_dimension.py
- array_shape.py
- array_dtype.py

## Concepts Covered

- ndim
- shape
- dtype

Upcoming

- size
- itemsize
- nbytes
- astype()

## 💡 Learning Outcome

After completing this example, you will understand:

- What dimensions are in NumPy
- Difference between 1D, 2D, and 3D arrays
- How to use the `.ndim` attribute

---

## 👨‍💻 Author

**Bharat Thakur**