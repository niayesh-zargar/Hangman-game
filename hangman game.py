# hangman
# list for names 
# len word
# how many trys 
# make a - for a right alphabet

import random 
list_words = ['banana','mango','apple' , 'orange','pear' , 'melon' , 'watermelon' ,'grapes']
pc_word = random.choice(list_words)
word = len (pc_word) * '-'
word = list(word)
GameRunning = True

def user_try():
    user_try = input("the alphabet : ").lower() 
    if user_try in pc_word :
        for index ,  char in enumerate(pc_word):
            if char == user_try :
                word[index] = user_try
    else:
        print("wrong choose")
        

    
while GameRunning :
    if '-' in word :
        print(word)
        user_try()
    else:
        print(f'word : {pc_word}')
        GameRunning = False
        print('thanks for playing.')
    