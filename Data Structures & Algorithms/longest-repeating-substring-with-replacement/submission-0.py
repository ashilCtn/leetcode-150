class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        left = 0
        maxLen = 0
        maxFreq = 0

        for right in range(len(s)):
            freq[ord(s[right]) - ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(s[right]) - ord('A')])

            windowLen = right - left + 1
            if windowLen - maxFreq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            windowLen = right - left + 1
            maxLen = max(maxLen, windowLen)
        
        return maxLen