class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (idx - index))
                start = index
            stack.append([start, h])

        for idx, height in stack:
            maxArea = max(maxArea, height * (len(heights) - idx))
        
        return maxArea


        