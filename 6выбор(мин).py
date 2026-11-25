def selection_sort(arr):
    print("Исходный вид:", arr)

    for i in range(len(arr)):
        min = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        
    print("Результат:", arr)

with open("input.txt", "r") as file:
    n = int(file.readline())
    numbers = list(map(int, file.read().split()))

selection_sort(numbers)
