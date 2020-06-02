# Write your code here
import random, string

print("H A N G M A N")

words_list = []                                                             
chances = 8                                                                
words = ['python', 'java', 'kotlin', 'javascript', "swift", "scala"]        
final_word = random.choice(words)                                           

hidden_word = "-" * len(final_word)                                         
word = final_word                                                           

print('Type "play" to play the game, "exit" to quit:')

while True:
    decision = input()

    if decision == 'play':
        while chances > 0 and final_word != hidden_word:
            print()
            print(hidden_word)
            guess = input("Input a letter: ")
            if len(guess) != 1:                                             
                print("You should input a single letter")
                continue
            if guess not in string.ascii_lowercase:                         
                print("It is not an ASCII lowercase letter")
                continue
            if guess in words_list:                                         
                print("You already typed this letter")
                chances -= 1
                print("You have ", chances, " chances.")
                continue
            words_list.append(guess)                                        
            while guess in word:
                n = word.index(guess)                                       
                word = word[:n] + "-" + word[n+1:]                          
                hidden_word = hidden_word[:n] + guess + hidden_word[n+1:]   
            if guess not in final_word:                                     
                print("No such letter in the word")
                chances -= 1
                print("You have ", chances, " chances.")

        if final_word == hidden_word:                                      
            print(final_word)                                               
            print("You guessed the word!")
            print("You survived!")
            break
        if final_word != hidden_word:                                       
            print("You are hanged!")
            break
    if decision == 'exit':                                                 
        break
