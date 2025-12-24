    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = []
        max_count = 0

        for char in s:
            if char in subString:
                index = subString.index(char)
                subString = subString[index + 1:]
            
            subString.append(char)
            
            max_count = max(max_count, len(subString))
            
        return max_count
        
