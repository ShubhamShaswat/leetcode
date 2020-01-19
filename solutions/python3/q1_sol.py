class Solutions:


    def twoSum(self,nums,target):

        #initialising ans with an empty list
        ans=[]
        #loop against the nums list
        for i in range(len(nums)):
            #loop agains the second num2
            #num[i] is the first number
            for j in  range(i+1,len(nums)):
                if nums[j] == target - nums[i]: #second number will be target - nums[i]

                    ans.append(i) #append the list with both index of the nums
                    ans.append(j)

        return ans
