class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, val in enumerate(temperatures):
            
            while stack and val > stack[-1][0]:
                tempVal, tempIdx = stack.pop()
                res[tempIdx] = idx - tempIdx

            stack.append([val, idx])
        
        return res
            
            
        