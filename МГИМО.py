# a, b = map(int, input().split())


# d = {'прр': '12', 'ссс': '11', 'ssw': '10', 't': 2}
# w_1 = d.keys() # получение ключа т.е то что до :
# w_2 = d.pop('t')
# w_3 = d.values()
# print(w_1, w_2, w_3, sep="\n")


numbers = [1, 2, 3, 4, 5]
ww = {x: [d for d in range(1, x + 1) if x % d == 0] for x in numbers}
print(ww)

res = {}
lst = []
for x in numbers:
    for d in range(1, x + 1):
        if x % d == 0:
            lst.append(d)
    res[d] = lst
print(x, lst, res)
# import numpy as np
# lst2 = []
# lst = np.array([[int(input()) for j in range(3)] for i in range(3)])
 
# print(*lst, sum(lst)) 
# for elem in lst:
#     for char in elem:
#         if char > np.mean(lst):
#             lst2.append(char)
# print(f'кол-во элементов больше ср. знач. {np.mean(lst)}: {len(lst2)}')











 









