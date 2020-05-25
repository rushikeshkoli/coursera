# python3
import sys

def BWT(text):
    n = len(text)
    text += text
    # print(text)
    cycles = ['gg'] * n
    # print(len(cycles))
    for i in range(n):
        cycles[i] = text[i:i + n]
        # print(cycles[i])
    cycles.sort()
    ans = ""
    for i in range(n):
        ans += cycles[i][n - 1]
    return ans

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))