# Створюємо класс.
class HashTable:
    # Створюємо функцію ініціації класу.
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False
    
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
