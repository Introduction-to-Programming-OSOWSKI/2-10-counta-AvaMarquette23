#WRITE YOUR CODE IN THIS FILE
def countA(w):
    y=0
    c=0
    for y in range(0,len(w)):
        if w[y]=="a":
            c=c+1
    return c
print(countA("cat"))