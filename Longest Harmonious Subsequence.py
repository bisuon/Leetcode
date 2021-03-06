#We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

#Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

#Example 1:
#Input: [1,3,2,2,5,2,3,7]
#Output: 5
#Explanation: The longest harmonious subsequence is [3,2,2,2,3].
#Note: The length of the input array will not exceed 20,000.
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#Learn how to use function collection.Counter(A)
#which A is a list
#the return is list which descrip the count numbers of each element in the list, like A = [1,2,3,43,3,4,2,434,1], 
#collection.Counter(A) = Counter({1: 2, 2: 2, 3: 2, 4: 1, 43: 1, 434: 1})
#while the length of Counter is equal to len（A）
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value = []
        c = collections.Counter(nums)
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if nums[i]+1 in nums:
                value.append(c[nums[i]]+c[nums[i]+1])
            
        # return max(value)
        if len(value)==0:
            return 0
        else:
            return max(value)
        # # for x in nums:
        # #     if x+1 in nums:
        # count = collections.Counter(nums)
        # value = 0
        # for x in count:
        #     if x+1 in count:
        #         value = max(value,count[x]+count[x+1])
        # return value
                
                
