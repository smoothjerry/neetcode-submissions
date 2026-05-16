class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list
        nums.sort()

        # track duplicates
        triplets = set()

        # select each num as a starting point
        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            # problem reduces to TwoSumII
            # find the rest of the triplet
            while l < r:
                if num + nums[l] + nums[r] > 0:
                    r -= 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    triplets.add((num, nums[l], nums[r]))
                    l += 1
        
        return list(triplets)


                