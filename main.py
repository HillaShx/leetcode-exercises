from datetime import datetime
from count_senior_passengers import Solution, input_data
# from max_score_for_removing_subs_old import Solution, input_data


def main():
    for i in input_data.keys():
        start_time = datetime.now()
        result = Solution().countSeniors(**input_data[i])
        end_time = datetime.now()
        print(f"input {i} | result: {result} | runtime: {end_time-start_time}")


if __name__ == "__main__":
    main()
