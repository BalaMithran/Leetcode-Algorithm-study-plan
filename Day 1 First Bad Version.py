class Solution:
    def firstBadVersion(self, n: int) -> int:
        start=1
        end = n
        while start<end:
            mid = (end+start)//2
            if isBadVersion(mid):
                end=mid
            else:
                start=mid+1
        return start
            
