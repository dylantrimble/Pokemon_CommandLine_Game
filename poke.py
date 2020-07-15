#Welcome to the world of Pokemans

from random import randint
import inquirer

def battle():
    pikachuHealth = 50
    userPokemon = 50
    print('\n Jeremy would like to battle.\n')
    print('\n Jeremy calls on Pikachu\n')
    while pikachuHealth > 0 or userPokemon > 0:
        answer = [
        inquirer.List('move',
                  message="Choose your move:",
                  choices=['Headbut', 'Tackle', 'Scratch'],
              ),
            ]

        move = inquirer.prompt(answer)['move']
        if move == 'headbut' or 'tackle' or 'sand attack':
            pikachuHealth = pikachuHealth - randint(5,20)
            print(f"\nYour pokemon used {move}, Jeremy's Pikachu now has {pikachuHealth} health left.")
            if pikachuHealth < 0:
                print("Jeremy's Pikachu fainted...")
                break
            elif userPokemon < 0:
                print(f"Your pokemon fainted.")
                break
            else:
                userPokemon = userPokemon - randint(5,20)
                print(f"\nJeremy's Pikachu used Tackle, your pokemon now has {userPokemon} health left.")
        else:
            print('\n Select a move!')
            answer = [
            inquirer.List('move',
                  message="Choose your move:",
                  choices=['Headbut', 'Tackle', 'Scratch'],
              ),
            ]

            move = inquirer.prompt(answer)['move']
            pikachuHealth = pikachuHealth - randint(5,20)
            print(f"\nYour pokemon used {move}, Jeremy's Pikachu now has {pikachuHealth} health left.")
            if pikachuHealth < 0:
                print("Jeremy's Pikachu fainted...")
                break
            else:
                userPokemon = userPokemon - randint(5,20)
                print(f"\n Jeremy's Pikachu used Tackle, your pokemon now has {userPokemon} health left.")
    if userPokemon > pikachuHealth:
        print(f'\n Jeremy: "Wow your pokemon is strong! I will win next time though!" \n Jeremy runs off.')
        print("\n You walk away and head toward the edge of town. You reach a sign that says 'Now Leaving the town of LittleRoot")
        print('\nThanks for playing, come back soon when we are done building the game.')
    else: 
        print('\n Jeremy: "I told you I was going to be the best didnt I?!" \n Jeremy runs off.')
        print('\nThanks for playing, come back soon when we are done building the game.')

def wildBattle(wildPokemon):
    
    wildPokemonHealth = 30
    userPokemon = 50
    print('\n Professor Birch: Quick! Help! There are pokeballs in the bag, pick one and help me!\n')
    answer = [
    inquirer.List('pokemon',
                  message="Choose your first Pokemon:",
                  choices=['Mudkip', 'Treecko', 'Torchic'],
              ),
        ]

    trainerPokemon = inquirer.prompt(answer)['pokemon']
    print(f'\nA wild {wildPokemon} appeard!\n')
    while wildPokemonHealth > 0 or userPokemon > 0:
        answer = [
        inquirer.List('move',
                  message="Choose your move:",
                  choices=['Headbut', 'Tackle', 'Scratch'],
              ),
            ]

        move = inquirer.prompt(answer)['move']
        if move == 'headbut' or 'tackle' or 'sand attack':
            wildPokemonHealth = wildPokemonHealth - randint(5,20)
            print(f"\n{trainerPokemon} used {move}, {wildPokemon} now has {wildPokemonHealth} health left.")
            if wildPokemonHealth < 0:
                print("Zigzagoon fainted...")
                break
            else:
                userPokemon = userPokemon - randint(5,20)
                print(f"\n{wildPokemon} used Tackle, {trainerPokemon} now has {userPokemon} health left.")
                if userPokemon < 0:
                    break
        else:
            print('\n Select a move!')
            answer = [
            inquirer.List('move',
                  message="Choose your move:",
                  choices=['Headbut', 'Tackle', 'Scratch'],
              ),
            ]

            move = inquirer.prompt(answer)['move']
            wildPokemonHealth = wildPokemonHealth - randint(5,20)
            print(f"\n{trainerPokemon} used {move}, {wildPokemon} now has {wildPokemonHealth} health left.")
            if wildPokemonHealth < 0:
                print(f"\nZigzagoon fainted...")
                break
            else:
                userPokemon = userPokemon - randint(5,20)
                print(f"\n {wildPokemon} used Tackle, {trainerPokemon} now has {userPokemon} health left.")
    if userPokemon > wildPokemonHealth:
        print(f'\nProfessor Birch: Thanks for saving me! That {wildPokemon} almost got me! Lets go back to my lab.')
        print('\nYou get back to the professors lab....')
        print(f'\nProf: Thanks so much for your help. You can keep {trainerPokemon}, you guys made a great team, and {trainerPokemon} will make a great companion. Goodluck on your Journey!')
        print('\nYou leave the lab.\n')
        print('\n You leave the Professors lab and begin to walk back home. \n unknown: "Hey you!" \n you turn and see a boy running up to you. \n unknown: "My name is Jeremy, I am the Professors nephew. I saw you leaving his lab, did you just get your first pokemon too?"')
        answer = [
            inquirer.List('answer',
                  message="did you just get your first pokemon too? ",
                  choices=['Yes', 'No'],
                    ),
                ]

        userAnswer = inquirer.prompt(answer)['answer']
        if userAnswer == 'Yes':
            print('\n Jeremy: COOL! I want to become the greatest trainer of all time. To do that I have to prove I can beat every trainer in a battle, starting with you!')
            battle()
        else:
            print("\n Jeremy: That's too bad. When you do, we should battle!")
            print("\n You walk away and head toward the edge of town. You reach a sign that says 'Now Leaving town!")
            print('Thanks for playing!!')
    else: 
        print(f'\n {trainerPokemon} fainted, you black out...')
        wildBattle(wildPokemon)

def professorBirch():
    print("\nYou walk to the Professor's lab, when you get there he isn't here. You see his assitant to the left\n")
    print("\nProfessor's Assistant: The Professor isn't here, he went into the feild to study wild pokemon. If you are looking for him he is on route 115.\n")
    answer = [
    inquirer.List('choice',
                  message="Do you want to go looking for the professor?",
                  choices=['Yes', 'No'],
              ),
        ]

    choice = inquirer.prompt(answer)['choice']

    if choice == 'Yes':
        print('You walk out the door and head to the edge of town.')
        wildPokemon = 'Zigzagoon'
        wildBattle(wildPokemon)   
    else:
        print('\nInvalid response\n')
        professorBirch()

def playGame():
    answer = [
            inquirer.List('answer',
                  message='Welcome to Pokemon! Do you want to play?',
                  choices=['Yes', 'No'],
                    ),
                ]

    userAnswer = inquirer.prompt(answer)['answer']
    print(userAnswer)
    if userAnswer == 'Yes':
        print('\nYou wake up in your new house and you hear your mom call you from downstairs.\n')
        answer = [
            inquirer.List('answer',
                  message='Go down stairs or stay in your room forever?',
                  choices=['stairs', 'room'],
                    ),
                ]

        userAnswer = inquirer.prompt(answer)['answer']
        if userAnswer == 'stairs':

            print('\nYou see your mom in the kitchen and approach her\n')
            print('\n"Mom: You woke up late! Professor Birch is waiting for you at his lab so you can get your first Pokemon!"\n')
            answer = [
            inquirer.List('answer',
                  message='Will you go see the professor or stay and chat with your mom?',
                  choices=['Mom', 'Professor'],
                    ),
                ]

            userAnswer = inquirer.prompt(answer)['answer']
            if userAnswer == 'Professor':
                professorBirch()
            else:
                print("\nMom: How are you liking LittleRoot so far? Your father wanted us to move here so you could meet Professor Birch. Speaking of, you need to go see him.")
                answer = [
                inquirer.List('answer',
                  message="Mom: Before you go see him though, how did you sleep last nigth?",
                  choices=['good', 'bad'],
                    ),
                ]

                userAnswer = inquirer.prompt(answer)['answer']
                print(userAnswer)
                if userAnswer == 'good':
                    print('\nMom:"Good!, then you shoudld be well rested enough to see professor Birch."\n')
                    professorBirch()
                else:
                    print('\nMom: go back up stairs and get some sleep.\n')
                    print("\nYou go upstairs and laydown...zZz...zZz...zZz")
                    print("\nYou awake well rested!")
                    professorBirch()
        else:
            print('\nLet us know when you feel like playing.\n')
    else:
        print('\nThats too bad.\n')


playGame()


questions = [
    inquirer.List('play',
                  message="Do you want to play again?",
                  choices=['yes', 'no'],
              ),
]

answers = inquirer.prompt(questions)['play']
if answers == 'yes':
    playGame()
else:
    print('Thanks again for playing!')

