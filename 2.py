def tupleLoop():
    t1 = ("apple", "banana", "cherry", "durian", "orange")
    for i in range(len(t1)):
        print("{} : {} ".format(i,t1[i]))

#~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sumComplex(a,b):
    c= (a[0] + b[0], a[1] + b[1])
    print("{} + {}i".format(c[0],c[1]))

#~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def multiComplex(a, b):
    c= (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
    print("{} + {}i".format(c[0],c[1]))

#~3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def inttuple(inttpl):
    for item in inttpl:
        if(isinstance(item,int)):
            print(item)
        elif(isinstance(item,tuple)):
            inttuple(item)


fruitlist = ["apple", "Strawberry", "banana", "raspberry","CHERRY", "banana", "durian", "blueberry"]
fruitlist.sort()
print( fruitlist )
fruitlist.sort( key=str.lower ) # case -insensitive sort
print( fruitlist )

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    # tupleLoop()
    a = (5,4)
    b = (6,2)
    inttpl = ( 1, 2, ( 3, 4 ), 5, ( ( 6, 7, 8, ( 9, 10 ), 11 ), 12, 13 ), ( ( 14, 15, 16 ), ( 17, 18, 19, 20 ) ) )
    sumComplex(a,b)
    # multiComplex(a, b)
    # inttuple(inttpl)