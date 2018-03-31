# this one doesn't make much sense in python

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        neg = False
        if dividend < 0:
            dividend = -dividend
            neg = ~neg
        if divisor < 0:
            neg = ~neg
            divisor = -divisor

        scale = 1
        scaled_divisor = divisor

        while dividend > scaled_divisor:
            scaled_divisor <<= 1
            scale <<= 1

        cnt = 0
        while dividend >= divisor and scaled_divisor >= divisor:

            while dividend >= scaled_divisor:
                dividend -= scaled_divisor
                cnt += scale

            scaled_divisor >>= 1
            scale >>= 1

        cnt = -cnt if neg else cnt

        if cnt >= 2147483647:
            return 2147483647
        return cnt
