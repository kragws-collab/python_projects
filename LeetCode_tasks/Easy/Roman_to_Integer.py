# roman = input()
roman = "IV"
summa = 0
dictionary = {"I": 1,
              "V": 5,
              "X": 10,
              "L": 50,
              "C": 100,
              "D": 500,
              "M": 1000}

for i in range(len(roman)):
    for j in dictionary.keys():
        if roman[i] == j :
            summa += dictionary[j]


print(summa)