# python3


def SiftDown(i, data, swaps):
    maxIndex = i
    l = 2 * i + 1
    if l < len(data) and data[l] < data[maxIndex]:
        maxIndex = l
    r = 2 * i + 2
    if r < len(data) and data[r] < data[maxIndex]:
        maxIndex = r
    if i != maxIndex:
        # print(i, ' ', maxIndex)
        swaps.append((i, maxIndex))
        data[i], data[maxIndex] = data[maxIndex], data[i]
        SiftDown(maxIndex, data, swaps)



def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        SiftDown(i, data, swaps)
        # print(data)
    return swaps
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
