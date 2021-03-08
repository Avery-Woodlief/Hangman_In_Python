from random import choice
import requests 

def main():
    print('Hangman\n')
    print('Rules: 1) Guess letters in a word.\n       2) Word length depends on difficulty.\n       3) If hangman is built before word, you lose.\n')
    global word, stage, spaces
    word, spaces = begin()
    stage = display(word)
    

def begin():
    '''
    Prompts user for specified game-mode:
    
    r: Randomly selected word from given website of 10000 words as well
    as random difficulty.
    
    w: User is allowed to specify difficulty level from 1 to 11 which controls the length of a randomly picked word
    which is not from given website.
    
    g: Complete gibberish is formed from English alphabet, however, user is allowed to declare difficulty.
    '''

    
    option = input('Random difficulty and word, just word, or complete gibberish? (r, w, or g): ')
    
    spaces = []

    if option == 'r':
        print("\nYou're brave, goodluck.")
        
        response = requests.get('https://www.mit.edu/~ecprice/wordlist.10000')
        word = response.content.splitlines()

        WORD = choice(word)

        gen_word = ''

        for k in range(len(WORD)):
            num = WORD[k]
            letter = chr(num)
            gen_word += letter

        word = gen_word
        
            
        for i in range(len(word)):
            spaces += ['_']
            
    elif option == 'w':
        length = int(input('Level of difficulty? (1 to 11): '))
        
        if length == 1:
            word = ['I', 'a', 'd', 'f', 'i', 'k', 'p', 't', 'u', 'y', 'z']
            word = choice(word)
        elif length == 2:
            word = ['VR', 'AI', 'hi', 'UV']
            word = choice(word)
        elif length == 3:
            word = ['fun', 'dad', 'act', 'age', 'ant', 'sun', 'son', 'cat', 'dog', 'man', 'tan', 'pan']
            word = choice(word)
        elif length == 4:
            word = ['math', 'cool', 'five', 'grey', 'foot', 'eyes', 'hand', 'code']
            word = choice(word)
        elif length == 5:
            word = ['Blows', 'Blown', 'Actor', 'fairy', 'tooth', 'color', 'light', 'hands', 'woman', 'stick', 'ghost']
            word = choice(word)
        elif length == 6:
            word = ['spider', 'friend', 'family', 'hangman', 'Pacman', 'screen', 'planet', 'banana', 'mashed', 'toggle', 'flower']
            word = choice(word)
        elif length == 7:
            word = ['Rainbow', 'fizzing', 'jazzman', 'Potatoe', 'mansion', 'Fallout', 'welcome', 'Ironman']
            word = choice(word)
        elif length == 8:
            word = ['Superman', 'computer', 'awesome!', "Batman's", 'Catwoman', 'Potatoes', 'survival', 'toggling']
            word = choice(word)
        elif length == 9:
            word = ['Spiderman', 'autoclick', 'Nutrition', 'education', 'Batmobile', 'blueberry','high five']
            word = choice(word)
        elif length == 10:
            word = ['bottle cap', 'strawberry','television', 'light rays', 'high fives']
            word = choice(word)
        elif length == 11:
            word = ['Intelligent', 'Environment', 'Shakespeare', 'Tooth Fairy', 'solar flare', 'code is fun', 'train track']
            word = choice(word)
        for i in range(len(word)):
            spaces += ['_']
            
    else:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        word = ''
        length = int(input('Level of difficulty? (1 to 11): '))
        for i in range(length):
            pick_letter = choice(letters)
            word += pick_letter
            spaces += ['_']
        

    return word, spaces





def display(word):
    '''
    There is were the action happens
    '''
    stage = 0
    r = 1
    
    misses = []
    guesses = []
    word1 = word
    game = True
    hangman(stage)
    print(spaces)
    while game:
        
        
        print('\n********************* ROUND {} *********************\n'.format(r))
        pick = input('\nPick a letter: ')
        guesses += pick
        
        if pick in word:
            while word.count(pick) >= 1:
                pos = word.index(pick)
                spaces[pos] = pick
                word = word.replace(pick, ' ', 1)
            hangman(stage)
            if word.count(' ') == len(word):
                print('\nWord: {}\nGuess: {}\nMisses: {}'.format(spaces, guesses, misses))
                print('\nYou win!')
                if len(misses) == 0:
                    print('\nWow, a perfect score!')
                break
        else:
            stage += 1
            hangman(stage)
            misses += pick
        r += 1
        print('\nWord: {}\nGuess: {}\nMisses: {}'.format(spaces, guesses, misses))
        if stage == 7:
            game = False
            print('\nYou lost!')
            print('\nWord was: {}'.format(word1))
       
    print('\n********************* GAME OVER *********************\n')
        
        
    return stage


def hangman(stage):
    '''
    These are the different stages of the hangman
    '''

    if stage == 0:
        print('\n               ___\n              |   |\n                  |\n                  |\n                  |\n                  |\n              ---------\n')

    elif stage == 1:
        print('\n               ___\n              |   |\n              O   |\n                  |\n                  |\n                  |\n              ---------\n')
        
    elif stage == 2:
        print('\n               ___\n              |   |\n              O   |\n              |   |\n                  |\n                  |\n              ---------\n')
        
    elif stage == 3:
        print('\n               ___\n              |   |\n              O   |\n             \\|   |\n                  |\n                  |\n              ---------\n')
        
    elif stage == 4:
        print('\n               ___\n              |   |\n              O   |\n             \\|/  |\n                  |\n                  |\n              ---------\n')
        
    elif stage == 5:
        print('\n               ___\n              |   |\n              O   |\n             \\|/  |\n              |   |\n                  |\n              ---------\n')
        
    elif stage == 6:
        print('\nLast chance!')
        print('\n               ___\n              |   |\n              O   |\n             \\|/  |\n              |   |\n             /    |\n              ---------\n')
        
    elif stage == 7:
        print('\n               ___\n              |   |\n              O   |\n             \\|/  |\n              |   |\n             / \\  |\n              ---------\n')


    
if __name__ == '__main__':
    main()
