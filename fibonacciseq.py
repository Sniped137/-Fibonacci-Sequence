total = 0
A = 1
B = 2
C = 0

while total < 4000000:
    C = A + B
    if C % 2 == 0:
        total += C  
    print(f"Next Number Extra in Sequence: {C}")
    A = B + C
    if A % 2 == 0:
        total += A
    print(f"Next Number Extra in Sequence: {A}")
    B = A + C
    if B % 2 == 0:
        total += B
    print(f"Next Number Extra in Sequence: {B}")
    print(total)

print(f"Final Total: {total}")





