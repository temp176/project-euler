nums = [i * j for i in range(100,1000) for j in range(100,1000)]
PalindromicNumbers = [nums[i] for i in range(0,len(nums)) if str(nums[i]) == str(nums[i])[::-1]]
max(PalindromicNumbers)