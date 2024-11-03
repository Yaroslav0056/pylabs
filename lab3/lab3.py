def find_dominator(arr):
    n = len(arr) // 2
    count_map = {}

    for num in arr:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
    print("Count map:", count_map)

    for num, count in count_map.items():
        if count > n:
            return num

    return -1

arr = [1, 3, 1, 3, 1, 3, 1, 3, 3]
print(find_dominator(arr))
