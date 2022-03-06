class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while(start<end):
            mid = (start+end )//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid
            else:
                start=mid+1
        if target>nums[-1]:
            return len(nums)
        else:
            return end
                
