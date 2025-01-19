class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        im = {}
        
        for i, j in enumerate(nums):
            if j in im and i - im[j] <= k:
                return True
            im[j] = i  
        
        return False