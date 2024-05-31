import re
## identify line returns '' if there is no match
def identify_line(expressions, current_line):
    result = ''
    for expression in expressions:
        x = re.search(expression, current_line)
        if x:
            print(current_line)
            print(x.group(0))
            result = expression
            break

    return result
