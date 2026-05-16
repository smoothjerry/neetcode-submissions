class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        
        longest = 0
        for num in nums:
            current = num
            currentLongest = 0
            exists = current in hashSet
            while exists:
                currentLongest += 1
                current = current + 1
                exists = current in hashSet
            
            longest = max(longest, currentLongest)
        
        return longest

