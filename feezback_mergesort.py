class Solution:
    def merge_sort(self, bigarr: list, smallarr: list) -> list:
        bigarr = sorted(bigarr)
        idx = len(bigarr) - 1
        while len(smallarr) > 0:
            if bigarr[idx] < smallarr[-1]:
                bigarr.insert(idx, bigarr.pop(0))
                bigarr[idx] = smallarr.pop(-1)
            idx -= 1
        return bigarr


input_data = {
    1: {
        "bigarr": [-1, 14, 17, -1, 28, -1, -1, 35, 36, 37, 81, 114, -1],
        "smallarr": [18, 22, 25, 66, 90],
    },
    2: {
        "bigarr": [14, 14, 28, -1, 35, 36, 37, 81, 114],
        "smallarr": [1],
    },
    3: {
        "bigarr": [14, 17, 28, 35, 36, 37, 81, 114],
        "smallarr": [],
    },
    4: {
        "bigarr": [14, 14, 17, -1, 28, -1, -1, 35, 36, 37, 81, 114, -1],
        "smallarr": [16, 22, 25, 66],
    },
    5: {
        "bigarr": [-1, 14, 17, -1, 28, -1, -1, 35, 36, 37, 81, 114, -1],
        "smallarr": [18, 22, 25, 66, 190],
    },
    6: {
        "bigarr": [114, -1],
        "smallarr": [190],
    }
}
