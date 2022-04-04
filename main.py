from feezback_mergesort import Solution, input_data


def main():
    solution = Solution()
    for i in input_data.keys():
        result = solution.merge_sort(**input_data[i])
        print(result)


if __name__ == "__main__":
    main()
