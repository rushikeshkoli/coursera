# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    j = 0
    for i, next in enumerate(text):
        # print(i)[][]
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))
            j += 1
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if(j == 0):
                return i + 1
            tp = opening_brackets_stack[j - 1]
            opening_brackets_stack.pop(j - 1)
            j -= 1
            if are_matching(tp.char, text[i]) == False:
                return i + 1
            pass

    if len(opening_brackets_stack) == 0:
        return -1
    else:
        return opening_brackets_stack[0].position


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == -1:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
