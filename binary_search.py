from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_idx = 0
        end_idx = len(nums)-1
        while end_idx > start_idx:
            middle_idx = start_idx + end_idx // 2
            if nums[middle_idx] == target:
                return middle_idx
            elif target > nums[middle_idx]:
                start_idx = middle_idx + 1
            elif target < nums[middle_idx]:
                end_idx = middle_idx - 1
        return -1


input_data = {
    1: {
        "nums": [-1, 0, 3, 5, 9, 12],
        "target": 9
    },
    2: {
        "nums": [-1, 0, 3, 5, 9, 12],
        "target": 2
    },
    3: {
        "nums": [],
        "target": 3
    },
    # 4: {
    #     "s": "",
    # },
    # 5: {
    #     "s": "((())",
    # },
    # 6: {
    #     "s": "]"
    # }
}