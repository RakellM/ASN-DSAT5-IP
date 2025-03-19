# %%

start = 1
end = 1000

while start <= end:

    if start == 11:
        start += 1
        continue

    if start % 11 == 0:
        break

    if start == 8:
        start += 1
        continue

    if start % 2 == 0:
        print(start, "é par!")

    start += 1