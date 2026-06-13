[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/TsfWRfvM)
# Geomatics Task - Python Geometry Package

This project is a Python package for working with basic geometry objects. It provides two main classes: **Point** and **Line**. You can create these objects, read them from files, and do simple geometry calculations with them.

---

## Project Purpose

The goal of this project is to show how to build a Python package with object-oriented programming. The package can:

- Create **Point** objects with x and y coordinates
- Create **Line** objects from multiple points
- Read geometry data from a text file
- Calculate the **total length** of a line
- Calculate the **perpendicular distance** from a point to a line

This project is useful for learning how to structure a Python package, write unit tests, and generate documentation.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.10+** | Main programming language |
| **math** | Built-in module for distance calculations |
| **unittest** | Writing and running tests |
| **Sphinx** | Generating HTML documentation |
| **sphinx-rtd-theme** | ReadTheDocs theme for documentation |
| **GitHub Actions** | Running tests automatically on every push |

---

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/GMT-211-Data-Structures-and-Algorithms/python-package-development-ii-nilisil.git
cd python-package-development-ii-nilisil
```

### 2. Create a Point

```python
from veri_odev import Point

p = Point(3.0, 4.0, "My Point")
print(p)  # Point(x=3.0, y=4.0, name='My Point')
```

### 3. Create a Line and Calculate Its Length

```python
from veri_odev import Point, Line

p1 = Point(0, 0)
p2 = Point(3, 4)

my_line = Line("My Line")
my_line.add_point(p1)
my_line.add_point(p2)

print(my_line.calculate_length())  # 5.0
```

### 4. Calculate Perpendicular Distance from a Point to a Line

```python
from veri_odev import Point, Line

p1 = Point(0, 0)
p2 = Point(3, 0)

my_line = Line("Horizontal Line")
my_line.add_point(p1)
my_line.add_point(p2)

outside_point = Point(1.5, 4)
distance = my_line.perpendicular_distance_to_point(outside_point)
print(distance)  # 4.0
```

### 5. Read Data from a File

You can read Point objects from a text file. The file must follow this format:

```
point
3
1.0,2.0,PointA
3.0,4.0,PointB
5.0,6.0,PointC
```

```python
from veri_odev import Point

points = Point.from_file("my_points.txt")
for p in points:
    print(p)
```

### 6. Run the Tests

```bash
python -m unittest discover tests
```

All tests are in the `tests/` folder. The tests check point creation, line length calculation, and perpendicular distance calculation.

---

## Author

**Nil Işıl Küçük** — 2026
