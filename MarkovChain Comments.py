import numpy as np
import sys
def Chain():
    options = ['','Markov_Source_Doc.txt','IntroToCyberThreatsModule6.txt', 'Programming_Week_6.txt', 'Programming_Week_7.txt']
    print('\n',
    '1. General Cyber Security','\n',
    '2. Cyber Threats Module 6; Encryption','\n',
    '3. Programming_Week_6','\n',
    '4. Programming_Week_7'
    )
    choose = int(input('Please choose which text you would like to simulate (1-4): '))
    chosen=(options[choose])
    comment = open(chosen, encoding='utf8').read()

    corpus = comment.split()

    def make_pairs(corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])
        
    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]
 
    first_word = np.random.choice(corpus)

    while first_word.islower():
        first_word = np.random.choice(corpus)

    chain = [first_word]
    while first_word.islower():
        first_word = np.random.choice(corpus)
    wordamount = int(input('Please enter the amount of words you would like your comment to consist of: '))
    n_words = wordamount

    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    ' '.join(chain)

    print(*chain)
    #with open('Comment_Output.txt', 'w', newline='') as f:
        #sys.stdout = f
        #print (*chain)
    f = open('Comment_Output.doc', 'a')
    print('------------------------------------------------------------','\n',chosen,'\n','------------------------------------------------------------','\n',*chain, '\n', file = f)
    f.close()

    enter=input('Press Enter to restart, otherwise, type anything and press enter to end: ')
    anything = 'a'
    if enter == '':
        Chain()
    if enter == anything:
        quit()

Chain()
