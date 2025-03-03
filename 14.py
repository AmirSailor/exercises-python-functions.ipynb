import inflect
n = 0
w = inflect.engine()
for i in range(0,1001):
    
    x = w.number_to_words(i)
    n += len(x.replace(" ","")) 
print(n)