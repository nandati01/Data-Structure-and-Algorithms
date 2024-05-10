from collections import defaultdict
def maxsum(nums):
    """
    Given an array of integer nums
    Return max value of nums[i] + nums[j] 
    where  nums[i] and nums[j] have the same digit sum
    Return -1 if there is no pair of numbers with the same digit sum
    """
    def get_digit_sum(num):
        sum = 0
        while num:
            sum += num % 10
            num //= 10
        return sum
    dic = defaultdict(int)
    ans = -1
    for num in nums:
        digit_sum = get_digit_sum(num)
        if digit_sum in dic:
            ans = max(ans, num + dic[digit_sum])
        dic[digit_sum] = max(dic[digit_sum], num)
    return ans
arr = [51, 42, 33, 24, 15]
print(maxsum(arr))
arr = [10, 20, 30, 40, 50]
print(maxsum(arr))
