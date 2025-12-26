    def reverse(self, x: int) -> int:
        sum = 0
        num = 0

        while(x != 0):
            if(x > 0):
                num = x % 10
                x = x // 10
                sum = sum * 10 + num
                if(sum < -2**31 or sum > (2**31)-1):
                    return 0
            else:
                num = x % -10
                sum = sum * 10 + num
                x = int(x / 10)
                if(sum < -2**31 or sum > (2**31)-1):
                    return 0
        return sum
