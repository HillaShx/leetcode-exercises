from grokking.one.get_max_subarray_avg import Solution, input_data


def main():
    solution = Solution()
    for i in input_data.keys():
        result = solution.findMaxAverage(**input_data[i])
        print(f"input {i} result: {result}")


if __name__ == "__main__":
    main()
