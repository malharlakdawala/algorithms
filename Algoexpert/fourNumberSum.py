from timer import timer


@timer
def fourNumberSum(array, targetSum):
    array.sort()
    dict = {}
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array) - 1):
            sum = array[i] + array[j]
            dict[sum] = (array[i], array[j])
    # print(dict)
    result_array = []
    temp_arr = []

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            sum = targetSum - array[i] - array[j]
            if sum in dict:
                temp_arr = [array[i], array[j], dict[sum][0], dict[sum][1]]
                temp_arr.sort()
                # temp_dict = set(temp_arr)
                # if len(temp_dict) == 4:
                if len(temp_arr)==len(set(temp_arr)) and temp_arr not in result_array:
                    result_array.append(temp_arr)
                temp_arr = []

    print(result_array)


fourNumberSum([7, 6, 4, -1, 1, 2], 16)

#
# for i in range(1,len(array)-1):
#     for j in range(i+1,len(array)):
#         pass

