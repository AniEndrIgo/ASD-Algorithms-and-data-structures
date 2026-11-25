def quick_sort(arr):
    print("Исходный массив:", arr)

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    result = quick_sort(left) + middle + quick_sort(right)

    return result


with open("input.txt", "r") as file:
    data = list(map(int, file.read().split()))

n = data[0]
numbers = data[1:]

numbers = quick_sort(numbers)

print("Результат:", numbers)