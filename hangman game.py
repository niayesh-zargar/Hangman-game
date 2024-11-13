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
count = len(pc_word) + 2


def user_try():
    user_try = input("the alphabet : ").lower() 
    if user_try in pc_word :
        for index ,  char in enumerate(pc_word):
            if char == user_try :
                word[index] = user_try
    else:
        print("wrong choose")
def comleted_word():
    global GameRunning
    user_completed_word = input("did you already know this word? yes or no \n").lower()
    if user_completed_word == 'yes' or user_completed_word == 'y':
        user_completed_word = input('word : ')
        if user_completed_word == pc_word :
            print('cheers to you.')
            GameRunning = False
        else :
            print('wrong one!')
            
    if user_completed_word == 'no' or user_completed_word =='n': 
        print('')
        
    
while GameRunning :
    if count >= 0 :
        
        if '-' in word :
            
            user_try()
            print(word)
            comleted_word()
        else:
            print(f'word : {pc_word}')
            GameRunning = False
            print('thanks for playing.')
        if '-' in word  and GameRunning :
            print(f"remainder try :{count}")
        count -= 1
    elif count < 0 :
        GameRunning = False
        print(f"game over\nword was {pc_word}")