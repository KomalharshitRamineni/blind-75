"""
dp-1d-bottomup — table over one index

Trigger: sequence DP where state is a single index — house robber, LIS, coin change, word break, decode ways. Complexity: O(n × transition)
"""



def dp_1d_bottomup(n):

    def base_case():
        return None

    
    state = [0] * (n + 1)          #Setting up the state space for the results of our subproblems

    state[0] = base_case(0)        # one base case per state the loop reads back
    state[1] = base_case(1)

    for i in range(2, n + 1):      # We build up solving smaller subproblems
        D1 = 1 + state[i - 1]      # Looking at the possible decisions we can make/our recursive function
        D2 = state[i - 2]
        state[i] = max(D1, D2)

    return state[n]
