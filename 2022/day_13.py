"""
--- Day 13: Distress Signal ---
"""

import general as g
import json


# all_packets = g.read_file("test_input.txt", False)
all_packets = g.read_file(split_lines=False)


def _compare_packet(left_list, right_lst):
    if not left_list and not right_lst:
        return None
    if not left_list:
        return True
    if not right_lst:
        return False

    left = left_list[0]
    right = right_lst[0]
    # print(f"comparing {left=} {right=}")

    if isinstance(left, list) and isinstance(right, list):
        val = _compare_packet(left, right)
        if val is not None:
            return val
    elif isinstance(left, list):
        val = _compare_packet(left, [right])
        if val is not None:
            return val
    elif isinstance(right, list):
        val = _compare_packet([left], right)
        if val is not None:
            return val
    else:
        # print(f"... {left=} {right=}")
        if left < right:
            return True
        elif right < left:
            return False

    return _compare_packet(left_list[1:], right_lst[1:])


def compare_packet(left_list, right_lst):
    ans = _compare_packet(left_list, right_lst)
    if ans is None:
        return True
    return ans


###########################################################
#
# MergeSort comes from the GeeksForGeeks article
# "Python Program for Merge Sort"
# I just modified it, replaced it's
# comparison function with my own (compare_packet).
# find original code here for it here:
# https://www.geeksforgeeks.org/python-program-for-merge-sort/
#
###########################################################
def merge(arr, l, m, r):
    """
    https://www.geeksforgeeks.org/python-program-for-merge-sort/
    """
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        # Changed comparison function
        if compare_packet(L[i], R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    """
    https://www.geeksforgeeks.org/python-program-for-merge-sort/
    """
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def part_one():
    count = 0
    for index, i in enumerate(all_packets.split("\n\n"), 1):
        if compare_packet(*(json.loads(x) for x in i.split())):
            count += index

    return count


def part_two():
    # load data
    packets = [json.loads(i) for i in all_packets.splitlines() if i]

    # inject divider packets
    DIVIDER_PACKETS = [
        [[2]],
        [[6]],
    ]
    packets.extend(DIVIDER_PACKETS)

    # sort all then find index of divider packets
    mergeSort(packets, 0, len(packets) - 1)
    answer = (packets.index(DIVIDER_PACKETS[0]) + 1) * \
        (packets.index(DIVIDER_PACKETS[1]) + 1)

    return answer


def main():
    g.print_parts(
        part_one(),
        part_two()
    )


main()
