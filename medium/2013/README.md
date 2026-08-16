# 2013. Detect Squares

You are given a stream of points on the X-Y plane. Design an algorithm that:

- **Adds**:  new points from the stream into a data structure. **Duplicate** points are allowed and should be treated as different points.
- Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.

An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the `DetectSquares` class:

- `DetectSquares()`: Initializes the object with an empty data structure.
- `void add(int[] point)`: Adds a new point  `point = [x, y]` to the data structure.
- `int count(int[] point)`: Counts the number of ways to form axis-aligned squares with point `point = [x, y]` as described above.

## Example 

```java
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // returns 1
detectSquares.count([14, 8]);  // returns 0
detectSquares.add([11, 2]);    // duplicate submissions are permitted
detectSquares.count([11, 10]); // returns 2
```

## Constraints

- `point.length == 2`
- `0 <= x, y <= 1000`
- At most `3000` calls in total will be made to `add` and `count`.