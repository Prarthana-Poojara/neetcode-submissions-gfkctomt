class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output =[]
        q = deque() 
        l =r = 0

        while r<len(nums):
            while q and nums[q[-1]]< nums[r]: # popping the smaller values from q
                q.pop()
            q.append(r) # append the element

            if l >q[0]:  #if the maximum value has exited the window then pop the element
                q.popleft()

            if (r+1)>=k: # make sure that the size if the window is k
                output.append(nums[q[0]]) #appened the largest value of the queue to the output list
                l +=1 
            r += 1

        return output



        