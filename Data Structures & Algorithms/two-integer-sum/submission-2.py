class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} # value --> index

        for i, n in enumerate (nums):
            indices[n] = i
        
        for i,n in enumerate(nums):
            diff = target - n # calculate the difference with each num in the list
            if diff in indices and indices[diff]!= i: # if the difference is in the dict and the indices are different
                return [i,indices[diff]]

        

        