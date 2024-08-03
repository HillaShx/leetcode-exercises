from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        win_size = nums.count(1)
        max_count = curr_count = sum(nums[:win_size])
        l_len = len(nums)
        for i in range(win_size, l_len + win_size):
            curr_count += nums[i % l_len]
            curr_count -= nums[(i - win_size) % l_len]
            max_count  = max(max_count, curr_count)
        return win_size - max_count


input_data = {
    # 1: {
    #     "nums": [0,1,0,1,1,0,0], # indices 1,3,4 gaps 4,2,1 -> 5,1,1
    # },
    # 2: {
    #     "nums": [0,1,1,1,0,0,1,1,0], # indices 1,2,3,6,7 gaps 3,1,1,3,1
    # },
    # 3: {
    #     "nums": [1,1,0,0,1], # indices 0,1,4 gaps 1,1,3  # wrapped
    # },
    # 4: {
    #     "nums": [1,0,0,0,1,0,1,0,1,0,1,0,1,0,1], # indices 0,4,6,8,10,12,14 gaps 1,4,2,2,2,2,2  # wrapped
    # }, # -> (6) 1,1,1,2,2,2 ->
    # 5: {
    #     "nums": [1,1,1,0,0,1,0,1,1,0], # indices 0,1,2,5,7,8 gaps 2,1,1,3,2,1  # if tipgap-1<=stranded->stranded
    # }, #
    # 6: {
    #     "nums": [1,1,1,0,0,0,1,0,1,0,1,1,0], # indices 0,1,2,6,8,10,11 gaps 2,1,1,4,2,2,1  #
    # },
    # 7: {
    #     "nums": [0,1,1,0,0,0,1,0,1,0,1,1,0], # indices 1,2,6,8,10,11 gaps 3,1,4,2,2,1
    # },
    # 8: {
    #     "nums": [0,0,1,0,0,0,0,0,1,0,1,1,0], # indices 2,8,10,11 gaps 4,6,2,1 -> 10,1,1,1
    # },
    # 9: {
    #     "nums": [0,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0],
    # },
    10: {
        "nums": [1],
    },
}
