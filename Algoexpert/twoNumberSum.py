def twoNumberSum(array, targetSum):
	if len(array)<=1:
		return []
	flag=0

	array = set(array)
	for arr in array:
		if targetSum-arr in array and targetSum!=2*arr:
			return [arr, targetSum-arr]
			flag=1
	if flag==0:
		return []
    # Write your code here.

twoNumberSum([4,5,6],6)
