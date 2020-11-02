# break在满足某一条件时，退出循环，不再执行后续重复代码。

i = 0 
while i < 10:
    if i == 3:
        break
    
    print(i)
    i += 1
print("Its over")

# continue在某一条件满足时，不再执行后续重复代码。
i = 0 
while i < 10:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

