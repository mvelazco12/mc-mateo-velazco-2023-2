A = set()
B = set()
C =set()
D =set()

A = {2,4,6,8,10,12,14,16,18,20,22,24}

B = {6,7,8,9,10,11,12,13,14,15,16,17,18,19}

C = {1, 4, 7, 8, 12, 16, 18, 21}

D = {2,3,5,7,11,13,17,19,23,29,31,37,41,43}

print("A ⋂(B⨁D)")
print(A.union(B.symmetric_difference(D)))

print("(B⋂C) ⋃D")    
print((B.intersection(C)).union(D))

print("(A⋃C) − B")
print((A.union(C)).difference(B))


print("(B − C) ⨁ (A ⋂ C)")
print((B.difference(C)).symmetric_difference(A.union(C)) )
