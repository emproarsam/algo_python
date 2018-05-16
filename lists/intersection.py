"""
Given 2 lists. Please find the intersection of the 2
"""


def intersection(seq1, seq2):

    # intersection12 = []
    # for i, vfi  in enumerate(seq1):
    #     for j, vfj in enumerate(seq2):
    #         if vfi == vfj:
    #             intersection12.append(vfi)
    return [vfi for i, vfi in enumerate(seq1) for j, vfj in enumerate(seq2) if vfi == vfj]
    # return intersection12


if __name__ == "__main__":
    input1 = [1,31,356,456,6754,8,679,7580579,875985]
    input2 = [1,31,356,456,6754,80,679,75809,8985]
    print(intersection(input1, input2))
