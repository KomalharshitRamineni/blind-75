"""
904. Fruit into baskets · https://leetcode.com/problems/fruit-into-baskets/
2026-11-09 · 20m · skeleton: sliding-window
O(n) time / O(1) space - We traverse through input and the max size of our basket is going to be 3, so known, therefore constant extra space
"""

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        

        basket = {}
        left = 0
        maxFruits = 0

        for right in range(len(fruits)):
            #We want to add this fruits
            basket[fruits[right]] = 1 + basket.get(fruits[right],0)
            
            #Now we check if more than two, if so, we keep removing left until its no longer true

            while left <= right and len(basket) > 2:
                #We decrement 
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])

                left+=1

            #Now at this point we are back to 2 distinc fruits
            maxFruits = max(maxFruits,(right-left)+1)

        return maxFruits

"""
    [1,2,3,2,2]
    {}

right=0     left = 0, {1:1}
right=1     left = 0, {1:1, 2,:1}     
right=2     left = 0, {1:1, 2:1, 3:1}
            {1:0, 2:1, 3:1} ==> {2:1, 3:1} left = 1
            max = right-left+1 => 2-1 = 1, +1 = 2

right=3     left = 1, {2:2, 3:1}        max = (3-1)  + 1
right=4     left = 1, {2:3, 3:1}        max = (4-1) + 1 = 4...

This alofirhtm runs in O(n) with O(1) space as constant size max 2?


"""
