class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        ans = []

        n = len(mat)       # Rows
        m = len(mat[0])    # Columns

        top, bottom = 0, n - 1
        left, right = 0, m - 1

        while top <= bottom and left <= right:
            # ➡ Top row - Left to Right
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1

            # ⬇ Right column - Top to Bottom
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1

            # ⬅ Bottom row - Right to Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(mat[bottom][i])
                bottom -= 1

            # ⬆ Left column - Bottom to Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])
                left += 1

        return ans
