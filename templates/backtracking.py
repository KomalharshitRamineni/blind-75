"""
backtracking — choose / explore / un-choose

Trigger: the output is a list of things — subsets, permutations, combinations, board placements, word search paths. If the answer is a count or an optimum, it's DP instead. That single discriminator resolves most backtracking-vs-DP confusion. Complexity: O(branching ^ depth)
"""


def backtracking():
    def foo():
        return True

    options = []
    res = []
    path = []

    def dfs(start):
        if foo(path):                  
            res.append(path.copy())     #.copy() as actual path keeps changing
            return
        if foo(start):                  # base case
            return

        for k in range(start, len(options)):   # Of all options available
            path.append(options[k])             #   choose
            dfs(k + 1)                          #   explore
            path.pop()                          #   un-choose

    dfs(0)

    return res
