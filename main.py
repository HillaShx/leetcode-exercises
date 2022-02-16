from delete_duplicates import Solution, input_data


def main():
    solution = Solution()
    for i in input_data.keys():
        result = solution.deleteDuplicates(**input_data[i])
        print(result)


if __name__ == "__main__":
    main()
