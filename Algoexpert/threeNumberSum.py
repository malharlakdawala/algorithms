def threeNumberSum(array, targetSum):
    right = len(array) - 1
    dict_array = set(array)
    result_array = []
    temp_array = []

    for i in range(len(array) - 2):
        for other_index in range(i + 1, len(array) - 1):
            result = targetSum - array[i] - array[other_index]
            if result in dict_array and array[i] != array[other_index] != result:
                temp_array = sorted([array[i], array[other_index], result])
                if temp_array not in result_array and len(temp_array)==len(set(temp_array)):
                    result_array.append(temp_array)
    return result_array


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))

# we have to send multiple combinations
# we have to stop the recurring patterns
# we have to stop recurring numbers


# right = len(array) - 1
# dict_array = set(array)
# result_array = []
# temp_array = []
#
# for i in range(len(array) - 2):
#     for other_index in range(i + 1, len(array) - 1):
#         result = targetSum - array[i] - array[other_index]
#         if result in dict_array and array[i] != array[other_index] != result:
#             temp_array = sorted([array[i], array[other_index], result])
#             if temp_array not in result_array and len(temp_array) == len(set(temp_array)):
#                 result_array.append(temp_array)
# return result_array

