def word_counter(wordlist):
    word_dic = {}

    for word in set(wordlist):
        word_dic[word] = wordlist.count(word)
    # print(wordlist)
    print(word_dic)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def str_word_counter(text):
    
    word_list = text.split(",")
    word_counter(word_list)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def translator():
    english_dutch = { "last":"laatst", "week":"week", "the":"de",\
        "royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":\
        "zaag", "first":"eerst", "performance":"optreden", "of":"van",\
        "a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij",\
        "one":"een", "world":"wereld", "leading":"leidend", "modern":\
        "modern", "composer":"componist", "composers":"componisten",\
        "two":"twee", "shed":"schuur", "sheds":"schuren" }

    sentence = "Last week The Royal Festival Hall saw the first \
        performance of a new symphony by one of the world's leading \
        modern composers, Arthur \"Two-Sheds\" Jackson." 
    string=""
    sentence.translate(str.maketrans('', '', string.punctuation))

    words = sentence.split()
    for i in range(len(words)):
        temp = english_dutch.get(words[i])
        if temp != None:
            words[i] = temp
    print(" ".join(words))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



if __name__ == '__main__':
    wordlist = ["apple","durian","banana","durian","apple","cherry",\
        "cherry","mango","apple","apple","cherry","durian","banana",\
        "apple","apple","apple","apple","banana","apple"]
    # word_counter(wordlist)

    text = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
        "apple,apple,cherry,durian,banana,apple,apple,apple," + \
        "apple,banana,apple"
    # str_word_counter(text)
    translator()