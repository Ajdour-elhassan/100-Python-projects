import random
words = ['advark' , 'baboon' , 'camel']

chosen_word = random.choice(words)

print(f'the chosen word is : {chosen_word}')

word_lenght = len(chosen_word)

display = []
for i in range(word_lenght):
    display += '_'
print(display)

stages = ["   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n"
    ,
"   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n"
          ,
"   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n"
          ,
"   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n"
          ,
"   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n"
          ,
          ]


live = 5
stage = ['Great +5' , 'Good' , 'Awesome +3' , 'excellent +2' , 'wondeful +1' ]

end_of_game = False

while end_of_game == False :

    guess = input('Quess a word : ').lower()

    if  guess in display :
        print(f'Good! you have alreaady guessed a letter {guess}')

    for position in range(word_lenght):
        # pass chosen_word to letter
        letter = chosen_word[position]
        # print(letter)
        if guess == letter:
            display[position] = letter
    #print(display)

    if guess not in chosen_word :
        print('you guess a wrong letter')
        live -= 1
        if live == 0 :
            end_of_game = True
            print('you lose')


    print(f"{' '.join(display)}")

    if '_' not in display :
        end_of_game = True
        print('you win')
    print(stage[live])