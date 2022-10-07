import random

a = int(input("请输入您要伪造的IP数量"))
c = []
for i in range(a):
    b = random.randint(0,9)
    c.append(b)
print(len(c))