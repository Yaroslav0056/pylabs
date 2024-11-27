def is_balanced_brackets(code):
    stack = []
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for char in code:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


code1 = "if (a > b) { return [1, 2, (3 + 4)]; }"
code2 = "if (a > b { return [1, 2, (3 + 4)]; }"
print(is_balanced_brackets(code1))
print(is_balanced_brackets(code2))
