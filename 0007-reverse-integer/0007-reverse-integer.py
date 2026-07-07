class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        neg=x<0
        if neg:
            x = -x

        while x:
            result=result*10+x%10
            x//=10

        if neg:
            result= - result

        return result if -2147483648<=result<=2147483647 else 0

        