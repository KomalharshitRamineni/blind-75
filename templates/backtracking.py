"""
backtracking — choose / explore / un-choose

Trigger: the output is a list of things — subsets, permutations, combinations, board placements, word search paths. If the answer is a count or an optimum, it's DP instead. That single discriminator resolves most backtracking-vs-DP confusion. Complexity: O(branching ^ depth)
"""


def backtracking():
    def foo():
        return None

    res = []
    path = []

    def dfs(index):
        if foo(index):                  
            res.append(path.copy())     #.copy() as actual path keeps changing
            return
            
        if not foo(index):                  # base case
            return
        
        path.append()
        dfs(index)                          # Decison A
        path.pop()
        dfs(index+1)                        # Decision B

    dfs(0)

    return res
