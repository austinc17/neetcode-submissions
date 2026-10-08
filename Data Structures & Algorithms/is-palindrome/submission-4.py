class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join([char for char in s if char.isalnum()])
        f=res.lower()
        p=''.join(reversed(f))
        return f==p
        

        