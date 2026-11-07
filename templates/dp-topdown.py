"""
dp-topdown — memoised recursion

Trigger: the default for any DP. Always write this first; tabulation is an optimisation you reach for second, and memoised recursion is usually an acceptable final interview answer. Four mechanical steps: 1. What arguments fully describe a subproblem? → that's your state 2. What's the answer at the smallest state? → base case 3. How does state N reduce to smaller states? → recurrence 4. Put `@cache` on it. The reason DP feels unwritable is almost always trying to fill a table directly. Don't. Complexity: O(states × transition cost)
"""


def dp_topdown():

    #We have some sort of function where we have subproblems that are being recomputed
    #So build up a tree in that form where the sub problems appear as nodes
    #Then we can memoise that

    def base_case():
        return None

    def dp(subproblem,cache):

        if subproblem in cache:
            return cache[subproblem]

        #other wise normal basecases for the problem

        if base_case():
            return 

        #Branches for decisions
        D1 = 1+ dp(subproblem + 1, cache)
        D2 = dp(subproblem + 2,cache)

        cache[subproblem] = max(D1,D2)

        return cache[subproblem]

    return dp(0,{})
