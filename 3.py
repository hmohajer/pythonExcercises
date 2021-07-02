import random


def magic_8ball():
    answers = [ "It is certain", "It is decidedly so", "Without a \
    doubt", "Yes, definitely", "You may rely on it", "As I see it, \
    yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
    "Reply hazy try again", "Ask again later", "Better not tell you \
    now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
    count on it", "My reply is no", "My sources say no", "Outlook \
    not so good", "Very doubtful" ]
    question= ["question 1 ?","question 2 ?","question 3 ?","question 4 ?"]
    index = random.randint(0,len(question)-1)
    print("question: {}".format(question[index]))
    index = random.randint(0,len(answers)-1)
    print("answers: {}".format(answers[index]))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def card_deck():
    numbers= []
    deck = []
    shuffuled_deck = []
    for i in range(2,11):
        numbers.append(i)
    for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]:
        for rank in numbers+[ "Jack", "Queen", "King", "Ace"]:
            deck.append((rank,suit))
    print(deck)
    for i in range(52):
        index = random.randint(0,len(deck)-1)
        shuffuled_deck.append(deck.pop(index))
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print(shuffuled_deck)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fifo():
    queue = []
    while 1==1 :
        command = input("your input or command sir: ")
        if command == "":
            break
        elif command == "?":
            if len(queue) > 0:
                print(queue.pop(0))
            else:
                print("sorry! there is nothing in the queue. try again")
        else:
            queue.append(command)
            print(" '{}' is added to the queue!".format(command))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def letter_counter():
    ...
    text = input("enter your text please: ")
    letters = set(text.lower())
    for letter in letters:
        # print(text.lower().count("k"))
        c = text.lower().count(letter)
        print("number of '{}' is : {}".format(letter, c))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# list of numbers => nbrs
#  nbrs[0] = 0
#  loop over list  find first not zero number
#  Now set all multiples of this number to zero
def eratosthenes(last):
    nbrs = list (range(1,last+1))
    nbrs[0] = 0
    for i in range(len(nbrs)):
        if nbrs[i] != 0:
            for j in range(i+1,len(nbrs)):
                if nbrs[j] != 0:
                    if nbrs[j]%nbrs[i] == 0 :
                        nbrs[j] = 0
    
    print(set(nbrs)-{0})
    # print((5,2)==(5,2))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == '__main__':
    # magic_8ball()
    # card_deck()
    # fifo()
    # letter_counter()
    eratosthenes(180)