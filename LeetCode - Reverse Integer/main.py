class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)[::-1]                                      
        y = str(abs(x))[::-1]      
        x = int('-' + y.strip('-')) if x < 0 else int(y)
        x = int('-' + y) if x < 0 else int(y)    
        return x if -2**31 < x < 2**31-1 else 0 
