# import math
# n = input()
# binary = []
# binary_final = []

# for i in n:
#     i = int(i)
#     while i > 1:
#         binary.append(i % 2)
#         i = math.floor(i/2)
#     binary.append(1)
#     if len(binary) < 3:
#         for j in range(3-len(binary)):
#             binary.append(0)
#     binary.reverse()
#     print(binary)
#     binary_final.extend(binary)
#     binary = []

# for num in binary_final:
#     print(num, end='')

print(bin(int(input(), 8)[2:]))