# def table(num): 
def table(): 
    num2 = int(input("give me a number: "))
    for i in range(1,11):
        # print("{} x {} = {}".format(i,num, i*num))
        print("{} x {} = {}".format(i,num2, i*num2))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def commonLetters(str1,str2):
    tempStr = ""
    count = 0
    str1 = str1.lower()
    str2 = str2.lower()
    for letter in str1:
        if(tempStr.find(letter) == -1):
            tempStr += letter
            if(str2.find(letter) != -1):
                print(letter)
                count += 1

    print("letter in common: {}".format(count))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def commonLetters2(str1,str2):
    tempStr = ""
    count = 0
    str1 = str1.lower()
    str2 = str2.lower()
    for letter in str1:
        if(not letter in tempStr):
            tempStr += letter
            if(letter in str2):
                print(letter)
                count += 1

    print("letter in common: {}".format(count))



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    # table(12)
    table()
    # a = input("str1: ")
    # b = input("str2: ")
    # commonLetters(a,b)
    # commonLetters2("pesolker","sekkeRaek")
