# Array Initialization in NumPy

## Overview

This folder demonstrates different ways to initialize NumPy arrays using built-in functions.

## Programs Included

### 1. full_array.py

Creates an array of a specified shape filled with a single value.

Example:

```python
np.full((3,2), 8)
```

---

### 2. ones_array.py

Creates an array filled with ones.

Example:

```python
np.ones((3,3))
```

---

### 3. zeros_array.py

Creates an array filled with zeros.

Example:

```python
np.zeros(5)
```

---
## 4. identity_matrix.py

Creates an identity matrix using NumPy.

### Syntax

```python
np.eye(size)
```

### Example

```python
import numpy as np

identity_matrix = np.eye(3)

print(identity_matrix)
```

### Output

```
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

### Use Cases

- Linear Algebra
- Matrix Operations
- Machine Learning
- Deep Learning

## Concepts Covered

- np.full()
- np.ones()
- np.zeros()
- Array Initialization
- Shape

## Requirements

- Python 3.x
- NumPy

Install NumPy

```bash
pip install numpy
```

## Author

**Bharat Thakur**