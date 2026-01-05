
def longgestCommonPrefix(self, strs: list[str]) -> str:
    if not strs:
            return ""
        
    prefix = strs[0]
        
    for i in range(1, len(strs)):
            # While the current word does not start with the prefix
            while not strs[i].startswith(prefix):
                # Shorten the prefix by one character from the end
                prefix = prefix[:-1]
                
                # If the prefix becomes empty, there is no common prefix
                if not prefix:
                    return ""
                    
    return prefix

    
strs = ["flower","flow","flight"]
longgestCommonPrefix(None, strs)

strs = ["dog","racecar","car"]
longgestCommonPrefix(None, strs)

strs = ["abca","aba","aaab"]
longgestCommonPrefix(None, strs)