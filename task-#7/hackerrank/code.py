#1

def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return alice, bob
alice_triplet = [5, 6, 7]
bob_triplet = [3, 6, 10]

alice, bob = compareTriplets(alice_triplet, bob_triplet)

print(f"score: ({alice},{bob})")

#2

def diagonal_difference(arr):
    n = len(arr)
    d1 = 0
    d2 = 0

    for i in range(n):
        d1 += arr[i][i]
        d2 += arr[i][n - i - 1]

    return abs(d1 - d2)


arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

result = diagonal_difference(arr)
print("Diagonal difference:", result)

