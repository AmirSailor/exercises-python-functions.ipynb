f = open('0089_roman.txt','r')
data = f.read()
datainlist = data.replace('\n', ' ').split(" ")

dic ={
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
    }

list2 = []
def RtoN(roman):
    prev_value = 0
    total = 0
    list1 = []
    for char in reversed(roman):
        value = dic[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total
list1 = [RtoN(roman) for roman in datainlist]

def NtoR(number):
    roman_pairs = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = []
    for value, numeral in roman_pairs:
        while number >= value:
            number -= value
            result.append(numeral)
    
    return ''.join(result)
list2 = [NtoR(number) for number in list1]

summ1 = 0
summ2 = 0
for i in datainlist:
    summ2 += len(i)
for i in list2:
    summ1 += len(i)
print(summ2-summ1)