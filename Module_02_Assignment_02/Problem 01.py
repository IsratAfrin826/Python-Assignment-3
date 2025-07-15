"""
Write a Python program that takes two sets from the user and computes their union, intersection, and difference.

A = {1, 2, 3, 4, 5}

B = {4, 5, 6, 7, 8}

"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union_result =  A.union(B)
intersection_result = A.intersection(B)
difference_A_B = A.difference(B)
difference_B_A = B.difference(A)

print("Set A:",A)
print("Set B:",B)
print("Union of A and B:", union_result)
print("intersection of A and B:", intersection_result)
print("Difference (A-B):", difference_A_B)
print("Difference (B-A):", difference_B_A)


