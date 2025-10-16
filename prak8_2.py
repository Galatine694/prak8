lines = []
for i in range(4):
    lines.append(input(f"Введіть рядок {i+1}: "))
def digit_sum(line):
    return sum(int(ch) for ch in line if ch.isdigit())
max_line = lines[0]
max_sum = digit_sum(lines[0])
for ln in lines[1:]:
    s = digit_sum(ln)
    if s > max_sum:
        max_sum = s
        max_line = ln
print("Рядок з найбільшою сумою цифр:", max_line)
print("Сума цифр у цьому рядку:", max_sum)