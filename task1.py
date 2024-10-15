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

# Створюємо хеш-таблицю розміром 10.
hash_table = HashTable(10)

# Додаємо елементи.
hash_table.insert("apple", 3)
hash_table.insert("banana", 5)
hash_table.insert("orange", 2)

# Отримуємо значення.
print("Значення для 'apple':", hash_table.get("apple"))  # Виведе: 3
print("Значення для 'banana':", hash_table.get("banana"))  # Виведе: 5
print("Значення для 'grape':", hash_table.get("grape"))  # Виведе: None, оскільки 'grape' немає в таблиці

# Видаляємо елемент.
print("Видалення 'orange':", hash_table.delete("orange"))  # Виведе: True
print("Значення для 'orange' після видалення:", hash_table.get("orange"))  # Виведе: None