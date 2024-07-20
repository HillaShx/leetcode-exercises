class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        x_value = 75
        y_value = 10
        init_sum = 115
        subs_x = int(init_sum / x_value)
        subs_y = int((init_sum - x_value * subs_x) / y_value)
        bob_wins = True
        overall_sum = x*x_value + y*y_value

        while overall_sum >= 115 and x >= subs_x and y >= subs_y:
            running_sum = 115
            running_sum -= subs_x * x_value
            x -= subs_x
            running_sum -= subs_y * y_value
            y -= subs_y
            bob_wins = not bob_wins
            overall_sum -= 115

        return get_winner_name(bob_wins)

def get_winner_name(bob_wins: bool):
    if bob_wins:
        return "Bob"
    else:
        return "Alice"




input_data = {
    1: {
        "x": 2,
        "y": 7,
    },
    2: {
        "x": 4,
        "y": 11,
    },
    3: {
        "x": 1,
        "y": 4
    }
}
