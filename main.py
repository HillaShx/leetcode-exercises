from datetime import datetime
from min_swaps_to_group import Solution, input_data


def main():
    for i in input_data.keys():
        start_time = datetime.now()
        result = Solution().minSwaps(**input_data[i])
        end_time = datetime.now()
        print(f"input {i} | result: {result} | runtime: {end_time-start_time}")


if __name__ == "__main__":
    main()
