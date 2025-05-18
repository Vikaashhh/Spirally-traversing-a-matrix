# 🚀 Day 36 - Spirally Traversing a Matrix
## 🧩 Problem Statement
Given a 2D matrix mat[][] of size n x m, return all elements of the matrix in spiral order — starting from the top-left and moving inward in a clockwise spiral.

## 📥 Input:
A rectangular matrix mat[][] of dimensions n x m.

## 📤 Output:
A list of integers representing the matrix traversed in spiral form.

## 🧠 Approach
We simulate the traversal by maintaining four boundaries:

- top → starting row index

- bottom → ending row index

- left → starting column index

- right → ending column index

We loop until all boundaries cross each other, and traverse in 4 directions:

1. ➡ Left to Right (Top Row)

2. ⬇ Top to Bottom (Right Column)

3. ⬅ Right to Left (Bottom Row)

4. ⬆ Bottom to Top (Left Column)

## 💡 Intuition:
Each boundary is updated after traversing in one direction, gradually moving the spiral inward.

## 🔍 Key Concepts Practiced
2D Array traversal

Boundary-based loop control

Simulation of direction-based movement

## ⏱ Time & Space Complexity
Time Complexity: O(n × m) — Every element is visited once

Space Complexity: O(1) — If output is not counted as extra spa

