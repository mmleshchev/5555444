def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def solution(a, b, c):
    if a + b == c:
        result = " С равна сумме A и B"
    else:
        result = "С не равна сумме A и B"
    return result

if __name__ == '__main__':
    print_hi('PyCharm')
    result = solution(1, 2, 3)
    print(result)
