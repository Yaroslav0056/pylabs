def is_balanced_brackets(code):
    stack = []
    flag = True

    for lt in code:
        if lt in "([{":
            stack.append(lt)
        elif lt in ")]}":
            if len(stack) == 0:
                flag = False
                break

            br = stack.pop()
            if br == '(' and lt == ')':
                continue
            if br == '[' and lt == ']':
                continue
            if br == '{' and lt == '}':
                continue

            flag = False
            break

    if flag and len(stack) == 0:
        return "Yes"
    else:
        return "No"

code1 = "if (a > b) { return [1, 2, (3 + 4)]; }"
code2 = "if (a > b { return [1, 2, (3 + 4)]; }"
print(is_balanced_brackets(code1))
print(is_balanced_brackets(code2))