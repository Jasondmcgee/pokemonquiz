def question1():
    print('Grass, Fire or Water?')
    print("Please enter a character a-c.")
    print("a.Grass")
    print("b.Fire")
    print("c.Water")
    answer = str(input(''))
    if (answer == 'a'):
        print('You must be a nature-lover whos one with the great outdoors!')
    elif (answer == 'b'):
        print('You are a lively, outgoing personality with a burning enthusiasm for the things you love most!')
    elif (answer == 'c'):
        print('You are chill and relaxed!')
    else:
        question1()
        print('please select a corresponding letter this time')
        

def question2():
    print('there are 240 pokemon in the orignal pokedex, right?')
    print('True or False')
    answer = str(input(''))

    if (answer == 'true' or answer == 'True'):
        print('you are NOT A REAL FAN, GO PLAY BAYBLADES')
    elif (answer == 'false' or answer == 'False'):
        print('Good job!')
    else: 
        print('type true or false please')

def question3():
    print('Your pokemon is poisoned going through the forest, what item do you use? Choose a letter a-d')
    print('a. Oran berry')
    print('b. antitdote')
    print('c. poke ball')
    print('d. bourban berry')
    answer = input('')
    if (answer == 'a'):
        print('wrong!')
    elif(answer == 'b'):
        print('right!')
    elif (answer == 'c'):
        print('wrong!')
    elif(answer == 'd'):
        print('wrong!')
    else:
        question3()
        print('type in a letter')
    

def question4():
    print('How many pokemon generations are there? give your answer as a number')
    answer = input('')
    if (answer == '7'):
        print('right!')
    else:
        print('aww almost got it, but the answer is 7!')

def question5():
    print('If you could take a vacation to any region, were would you go?')
    answer = input('')
    print('I really liked the ' + answer + ' region too!')

def question6():
    print('Who is your favorite professor?')
    print('a. professor Oak')
    print('b. professor Birch')
    print('c. professor Jess')
    answer = str(input(''))
    answer = answer.strip(' ')
    if (answer == 'c'):
        print('thats my favorite professor too!')
    else:
        print('meh, I thought another professor was better')

def question7():
    print('True of False, a Kakuna evolves into a Butterfree.')
    answer = str(input(''))

    if (answer == 'true' or answer == 'True'):
        print('Incorrect! A Kakuna evolves into a Beedrill bzzzzzzz')
    elif (answer == 'false' or answer == 'False'):
        print('Good job! You know your evolutions')
    else: 
        print('type true or false please')

def question8():
    print('What year was the first Pokemon game released? Enter your answer as a number')
    answer = input('')
    if (answer == '1996'):
        print('right!')
    else:
        print('Nope! The first Pokémon games, Pokémon Red and Green Versions, came to the Nintendo Game Boy system in Japan on February 27, 1996')

def quiz():
    print('Pokemon quiz')

    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
    question8()

def response():
    print('incomplete')


quiz()