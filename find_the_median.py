    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen = len(nums1) + len(nums2)
        combinedNums = nums1 + nums2
        combinedNums.sort()
        mid = totalLen // 2
        if(totalLen  % 2 != 0):
            return float(combinedNums[mid])
        else:
            return (combinedNums[mid - 1] + combinedNums[mid])/2.0
