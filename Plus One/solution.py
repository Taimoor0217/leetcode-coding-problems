class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits) - 1
        while digits[j] == 9:
            digits[j] = 0
            j -= 1
        if j >= 0:
            digits[j] += 1
        else:
            digits = [1] + digits
        return digits