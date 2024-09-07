# a, b = map(int, input().split())

numbers = [1, 2, 3, 4, 5]
ww = {x: [d for d in range(1, x + 1) if x % d == 0] for x in numbers}
print(ww)

import numpy as np
lst2 = []
lst = np.array([[int(input()) for j in range(3)] for i in range(3)])
 
print(*lst, sum(lst)) 
for elem in lst:
    for char in elem:
        if char > np.mean(lst):
            lst2.append(char)
print(f'кол-во элементов больше ср. знач. {np.mean(lst)}: {len(lst2)}')











 









