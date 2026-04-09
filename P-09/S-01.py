class Solution:
    def isPalindrome(self, x: int) -> bool:
        l1 = list(str(x))
        l2 = l1.copy()
        l2.reverse()
        if l1 == l2:
            return True
        else:
            return False
        
        

        