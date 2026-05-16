class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        
        longest = 0
        for num in nums:
            current = num
            currentLongest = 0
            while current in hashSet:
                currentLongest += 1
                current = current + 1
            
            longest = max(longest, currentLongest)
        
        return longest

