# Write your code here
import random, string

print("H A N G M A N")

words_list = []                                                             # list of used words
chances = 8                                                                 # number of chances
words = ['python', 'java', 'kotlin', 'javascript', "swift", "scala"]        # possible words for guessing
final_word = random.choice(words)                                           # random selected word

hidden_word = "-" * len(final_word)                                         # hidden word variable
word = final_word                                                           # word variable which will be change into hidden word

print('Type "play" to play the game, "exit" to quit:')

while True:
    decision = input()

    if decision == 'play':
        while chances > 0 and final_word != hidden_word:
            print()
            print(hidden_word)
            guess = input("Input a letter: ")
            if len(guess) != 1:                                             # guess should have length = 1
                print("You should input a single letter")
                continue
            if guess not in string.ascii_lowercase:                         # guess should be an ASCII lowercase letter
                print("It is not an ASCII lowercase letter")
                continue
            if guess in words_list:                                         # guess can't be already guessed
                print("You already typed this letter")
                chances -= 1
                print("You have ", chances, " chances.")
                continue
            words_list.append(guess)                                        # adding guess into word_list
            while guess in word:
                n = word.index(guess)                                       # index of guess in word
                word = word[:n] + "-" + word[n+1:]                          # changing guess in word into '-'
                hidden_word = hidden_word[:n] + guess + hidden_word[n+1:]   # unhidding place with guessed letter
            if guess not in final_word:                                     # guess should be in our selected word
                print("No such letter in the word")
                chances -= 1
                print("You have ", chances, " chances.")

        if final_word == hidden_word:                                       # selected word and unhidden word are equal,
            print(final_word)                                               # someone have guessed word.
            print("You guessed the word!")
            print("You survived!")
            break
        if final_word != hidden_word:                                       # end of chances, someone is hanged
            print("You are hanged!")
            break
    if decision == 'exit':                                                 
        break