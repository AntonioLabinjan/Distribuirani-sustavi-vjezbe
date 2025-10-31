def primes_in_range(start, end):
    if end < 2:
        return []

    # Korak 1: Pretpostavi da su svi brojevi prosti
    prost = [True] * (end + 1)
    prost[0] = prost[1] = False  # 0 i 1 nisu prosti

    # Korak 2: Sito - eliminiramo višekratnike
    for i in range(2, int(end ** 0.5) + 1):
        if prost[i]:
            for j in range(i * i, end + 1, i):
                prost[j] = False

    # Korak 3: Vraćamo sve koji su True u danom rasponu
    return [i for i in range(start, end + 1) if prost[i]]


# Primjer
print(primes_in_range(1, 30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]