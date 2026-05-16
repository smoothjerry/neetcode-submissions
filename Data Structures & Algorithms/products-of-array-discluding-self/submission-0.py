class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        for i in range(1, len(pref)):
            pref[i] = pref[i - 1] * nums[i - 1]
        
        suf = [1] * len(nums)
        for i in range(len(suf) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        
        exceptSelf = [1] * len(nums)
        for i in range(len(exceptSelf)):
            exceptSelf[i] = pref[i] * suf[i]

        return exceptSelf
        