#num = int(input())

num = 1110001113333222

from itertools import groupby
from collections import Counter


def change(num):
    num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    return num2words[num]

dic = {}
res = []

for i,j in groupby(str(num)):
    j = list(j)
    res.append(change(len(j))+" "+i+"'s")
print(" and ".join(res))



total = dict(Counter(str(num)))
tot = []
print("Total: ",end="")
for i,j in total.items():
    tot.append(change(j)+" "+i+"'s")
print(" and ".join(tot))
