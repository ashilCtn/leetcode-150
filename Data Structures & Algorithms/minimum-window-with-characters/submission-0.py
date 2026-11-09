class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '' : return ''
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        need, having = len(countT), 0
        res, resLen = [-1, -1], float('inf')

        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                having += 1
            
            while having == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    having -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float('inf') else ""