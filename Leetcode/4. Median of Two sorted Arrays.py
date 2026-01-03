#Approach - 1

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)
        nums1.sort()

        n = len(nums1)
        mid = n//2

        if n % 2 == 1:
            return nums1[mid]

        else:
            return (nums1[mid]+nums1[mid-1])/2
