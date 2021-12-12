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



  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.


  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.

  You can assume that there will be at most one pair of numbers summing up to
  the target sum.

two_number_sum([3,5,-4,8,11,1,-1,6],10)
>> [-1,11]
