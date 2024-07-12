from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avgs = []
        sub_sum = 0
        i = 0
        e = int(k)
        while i < len(nums):
            if i < e:
                sub_sum += nums[i]
                i+=1
            else:
                avgs.append(sub_sum / k)
                sub_sum-=nums[i-k]
                e+=1
        avgs.append(sub_sum / k)
        return max(avgs)

input_data = {
    1: {
        "nums": [-1, 14, 17, -1, 28, -1, -1, 35, 36, 37, 81, 114, -1],
        "k": 3,
    },
    2: {
        "nums": [4, 0, 4, 3, 3],
        "k": 5,
    },
    3: {
        "nums": [14, 17, 28, 35, 36, 37, 81, 114],
        "k": 1,
    },
    4: {
        "nums": [14, 14, 17, -1, 28, -1, -1, 35, 36, 37, 81, 114, -1],
        "k": 4,
    },
    5: {
        "nums": [-1, 14, 17, -1, 28, -1, -1, 35, 36, 37, 81, 114, -1],
        "k": 3,
    },
    6: {
        "nums": [114, -1],
        "k": 2,
    }
}
