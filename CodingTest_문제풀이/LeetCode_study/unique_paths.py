"""
https://leetcode.com/problems/unique-paths/submissions/
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = (m - 1) + (n - 1)
        N_fact = 1
        for i in range(1, N + 1):
            N_fact = N_fact * (i)

        m_fact = 1
        for i in range(1, m):
            m_fact = m_fact * (i)

        n_fact = 1
        for i in range(1, n):
            n_fact = n_fact * (i)

        answer = N_fact // (m_fact * n_fact)
        return answer


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = (m - 1) + (n - 1)
        N_fact = 1
        for i in range(1, N + 1):
            N_fact = N_fact * (i)

        for i in range(1, m):
            N_fact = N_fact // i

        for i in range(1, n):
            N_fact = N_fact // i

        return N_fact


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = (m - 1) + (n - 1)
        N_fact = 1
        for i in range(N, m - 1, -1):
            N_fact = N_fact * (i)

        for i in range(1, n):
            N_fact = N_fact / i

        return int(N_fact)
