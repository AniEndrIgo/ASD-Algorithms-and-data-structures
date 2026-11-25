def shell_sort(arr):
    print("Исходный вид:", arr)

    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

            print(arr)

        gap //= 2

    print("Результат:", arr)


with open("input.txt", "r") as file:
    data = list(map(int, file.read().split()))

n = data[0]
numbers = data[1:]

shell_sort(numbers)
