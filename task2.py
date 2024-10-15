#  Реалізація двійкового пошуку для відсортованого масиву.
    
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
        
    while left <= right:
        mid = (left + right) // 2
        iterations += 1
            
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
                
    return (iterations, upper_bound)

# Відсортований масив.
arr = [1, 3, 5, 7, 9, 11, 13, 15]

# Цільове значення, яке потрібно знайти.
target = 10

# Виклик функції.
iterations, result = binary_search(arr, target)

# Виведення результату.
print(f"Кількість ітерацій: {iterations}")
print(f"Результат: {result}")