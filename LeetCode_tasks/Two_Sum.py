array = input().split()
target = int(input())

lst = []
bp = True
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if int(array[i]) + int(array[j]) == target and bp == True:
            lst.append(i)
            lst.append(j)
            bp = False

print(lst)
