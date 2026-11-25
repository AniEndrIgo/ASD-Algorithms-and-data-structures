def merge_sort(arr):
    print("Исходный вид:", arr)

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

with open("input.txt", "r") as file:
    data = list(map(int, file.read().split()))

n = data[0]
numbers = data[1:]

numbers = merge_sort(numbers)

print("Результат:", numbers)
