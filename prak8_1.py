s1 = input("Введіть перший рядок слів: ")
s2 = input("Введіть другий рядок слів: ")
def remove_duplicates(line):
    words = line.split()
    unique = []
    for w in words:
        if w not in unique:
            unique.append(w)
    return " ".join(unique)
result1 = remove_duplicates(s1)
result2 = remove_duplicates(s2)
print("Результат для першого рядка:", result1)
print("Результат для другого рядка:", result2)