"""
dp-2d-grid — table over two indices

Trigger: two sequences (edit distance, LCS, interleaving) · a grid with directional moves · knapsack with capacity as the second axis. Complexity: O(n × m)
"""



def dp_2d_grid(m, n):

    def base_case(i, j):
        return None

    state = [[0] * n for _ in range(m)]   # state[i][j] = <meaning>, one fresh row per i

    for i in range(m):                    # edges: only one way in, fill first
        state[i][0] = base_case(i, 0)
    for j in range(n):
        state[0][j] = base_case(0, j)

    for i in range(1, m):                 # row by row: above and left are already final
        for j in range(1, n):
            D1 = state[i - 1][j]          # from above
            D2 = state[i][j - 1]          # from the left
            state[i][j] = max(D1, D2)

    return state[m - 1][n - 1]
