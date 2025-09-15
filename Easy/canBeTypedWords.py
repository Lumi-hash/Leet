from typing import List

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        brokenList = list(brokenLetters)

        count = 0
        for word in words:
            can_type = True   
            
            for ch in word:   
                if ch in brokenList:
                    can_type = False
                    break     
            
            if can_type:
                count += 1

        return count
        
# --- test ---
s = Solution()

print(s.canBeTypedWords("hello world", "ad"))   # expect 1
print(s.canBeTypedWords("leet code", "lt"))     # expect 1
print(s.canBeTypedWords("leet code", "e"))      # expect 0