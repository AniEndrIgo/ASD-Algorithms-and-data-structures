def comb_sort(arr):
    print("Исходный вид:", arr)

    gap = len(arr)
    shrink = 1.3
    sorted = 0

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = 1

        i = 0

        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = 0

            i += 1
    print("Результат:", arr)

with open("input.txt", "r") as file:
    n = int(file.readline())
    numbers = list(map(int, file.read().split()))

comb_sort(numbers)
