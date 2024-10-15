# Імпортуємо лібу!
import timeit

# Відкриваємо файли тільки на читання.
with open('стаття1.txt', 'r', encoding='ISO-8859-1') as file:
    text1 = file.read()
with open('стаття2.txt', 'r', encoding='ISO-8859-1') as file:
    text2 = file.read()

existing_substring = "Автори публiкації"  # існуючий підрядок
non_existing_substring = "вигаданий підрядок"

# Створюємо функції алгоритмів.
def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0:
        return -1

    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    skip = {c: m for c in set(text)} | skip

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += skip.get(text[i + m - 1], m)
    
    return -1

def knuth_morris_pratt_search(text, pattern):
    m = len(pattern)
    n = len(text)

    if m == 0:
        return -1

    lps = [0] * m
    j = 0

    def compute_lps(pattern, m, lps):
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

    compute_lps(pattern, m, lps)
    
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1

def rabin_karp_search(text, pattern, prime=101):
    m = len(pattern)
    n = len(text)
    d = 256
    h = 1
    p = 0
    t = 0

    for i in range(m - 1):
        h = (h * d) % prime

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t < 0:
                t += prime

    return -1

# Функція для вимірювання часу виконання кожного з алгоритмів.
def measure_time(algorithm, text, substring):
    timer = timeit.Timer(lambda: algorithm(text, substring))
    return timer.timeit(number=1)

# Словник для зручності виклику функцій алгоритмів.
algorithms = {
    "Boyer-Moore": boyer_moore_search,
    "Knuth-Morris-Pratt": knuth_morris_pratt_search,
    "Rabin-Karp": rabin_karp_search
}

# Збереження результатів.
results = {
    "стаття1": {
        "existing": {},
        "non_existing": {}
    },
    "стаття2": {
        "existing": {},
        "non_existing": {}
    }
}

# Виконання алгоритмів для кожного підрядка в обох текстах.
for name, func in algorithms.items():
    # Існуючий підрядок в тексті 1
    results["стаття1"]["existing"][name] = measure_time(func, text1, existing_substring)
    # Вигаданий підрядок в тексті 1
    results["стаття1"]["non_existing"][name] = measure_time(func, text1, non_existing_substring)
    # Існуючий підрядок в тексті 2
    results["стаття2"]["existing"][name] = measure_time(func, text2, existing_substring)
    # Вигаданий підрядок в тексті 2
    results["стаття2"]["non_existing"][name] = measure_time(func, text2, non_existing_substring)

# Вивід результатів
print("Результати для тексту 1 з існуючим підрядком:", results["стаття1"]["existing"])
print("Результати для тексту 1 з вигаданим підрядком:", results["стаття1"]["non_existing"])
print("Результати для тексту 2 з існуючим підрядком:", results["стаття2"]["existing"])
print("Результати для тексту 2 з вигаданим підрядком:", results["стаття2"]["non_existing"])
