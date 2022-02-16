from add_two_numbers import Solution

input_data = {}


def main():
    solution = Solution()
    for i in range(1, 6):
        result = solution.addTwoNumbers(input_data[i]["l1"], input_data[i]["l2"])
        print(result)


if __name__ == "__main__":
    main()
