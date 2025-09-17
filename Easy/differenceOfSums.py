class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0

        for num in range(0,n + 1):
            if num % m != 0:
                num1 += num
            else:
                num2 += num
    
        return num1 - num2

# -- test -- 
s = Solution()
print(s.differenceOfSums(10,3)) #expect 19
print(s.differenceOfSums(5,6)) #expect 15
print(s.differenceOfSums(5,1)) #expect -15
