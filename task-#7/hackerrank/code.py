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

