class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        current = 0
        while current < len(nums):
            if nums[current] == val:
                nums.pop(current)
            else:
                current +=1
            
        return len(nums)