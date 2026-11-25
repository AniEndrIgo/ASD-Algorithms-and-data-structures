def insertion_sort(arr):
    print("Исходный вид:", arr)

    for i in range(1, len(arr)):
        right = arr[i]
        left = i - 1

        while left >= 0 and arr[left] > right:
            arr[left + 1] = arr[left]
            left -= 1

        arr[left + 1] = right

with open("input.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

insertion_sort(numbers)

with open("output.txt", "w") as file:
    file.write(" ".join(map(str, numbers)))

print("Результат:", numbers)