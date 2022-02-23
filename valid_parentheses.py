from typing import Optional

parentheses_dictionary = {
    '(': ')',
    '[': ']',
    '{': '}',
}


class ParenthesesValidationStack:
    def __init__(self, value: str = ""):
        self.value = value

    def __str__(self):
        return self.value

    def is_empty(self) -> bool:
        return len(self.value) == 0

    def push(self, char: str) -> None:
        self.value += char

    def get_last_char(self) -> Optional[str]:
        if not self.is_empty():
            return self.value[-1]

    def pop(self) -> Optional[str]:
        if not self.is_empty():
            popped_value = self.value[-1]
            self.value = self.value[:-1]
            return popped_value


class Solution:
    def isValid(self, s: str) -> bool:
        stack = ParenthesesValidationStack()
        invalid_input = False
        for char in s:
            if invalid_input:
                break
            if char in parentheses_dictionary.keys():
                stack.push(char)
            elif char in parentheses_dictionary.values():
                if stack.is_empty():
                    invalid_input = True
                    break
                last_char = stack.get_last_char()
                if not (char == parentheses_dictionary[last_char]):
                    invalid_input = True
                    break
                stack.pop()
        return stack.is_empty() and not invalid_input


input_data = {
    1: {
        "s": "([{}])",
    },
    2: {
        "s": "()[{}]",
    },
    3: {
        "s": "(()]{}",
    },
    4: {
        "s": "",
    },
    5: {
        "s": "((())",
    },
    6: {
        "s": "]"
    }
}