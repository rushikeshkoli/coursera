# python3
import sys

def InverseBWT(bwt):
    # write your code here
    counter = [0] * 5
    arr = [0] * len(bwt)
    offset = {'A': 1, 'C': 2, 'G': 3, 'T': 4, '$': 0}
    temp = [0] * 5
    for i in range(len(bwt)):
        arr[i] = counter[offset[bwt[i]]]
        counter[offset[bwt[i]]] += 1
    for i in range(1, 5):
        temp[i] = temp[i - 1] + counter[i - 1]

    ans = "$"
    j = 0
    for i in range(1, len(bwt)):
        ans += bwt[j]
        # j = counter[offset[bwt[j]]]
        j = temp[offset[bwt[j]]] + arr[j]

    return ans[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))