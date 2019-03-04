import random
from random import shuffle

#Introduction to the game
print("------------------------------------------------------------------------------------------------------------------------")
print("\nGOAL: Correctly guess the order with as few hints as possible, but be careful you're only allowed one guess!\n \nINSTRUCTIONS: Press enter to get a new hint or type a guess.")

game = True #Variable that allows for a game restart

while game:

    loop = True #Variable that loops the questions
    numberOfHints = 0 #Keeps track of number of hints used
    pos = 0 #Variable that decides what hint to give
    print("\nWORDBANK: Hemiptera Hymenoptera Diptera Lepidoptera Coleoptera Orthoptera Odonata")  #WORDBANK for spelling

    #Array of the arthropod orders
    orders = ["Hemiptera","Hymenoptera","Diptera","Lepidoptera","Coleoptera","Orthoptera","Odonata"]

    #The hints given array
    hemipteraHints = ["HEMI1","HEMI2","HEMI3","HEMI4","HEMI5"]
    hymenopteraHints = ["HYM1","HYM2","HYM3","HYM4","HYM5"]
    dipteraHints = ["DIP1","DIP2","DIP3","DIP4","DIP5"]
    lepidopteraHints = ["LEP1","LEP2","LEP3","LEP4","LEP5"]
    coleopteraHints = ["COLE1","COLE2","COLE3","COLE4","COLE5"]
    orthopteraHints = ["ORTHO1","ORTHO2","ORTHO3","ORTHO4","ORTHO5"]
    odonataHints = ["ODON1","ODON2","ODON3","ODON4","ODON5"]

    #Moving all questions into one variable to store them
    allHints = list(zip(hemipteraHints, hymenopteraHints, dipteraHints, lepidopteraHints, coleopteraHints, orthopteraHints, odonataHints))

    #Shuffling the questions so that they are random
    selection = random.choice(orders)
    random.shuffle(allHints)
    hemipteraHints, hymenopteraHints, dipteraHints, lepidopteraHints, coleopteraHints, orthopteraHints, odonataHints = zip(*allHints)

    #IF statements that go though the possible questions and display them
    while loop:
        if selection == "Hemiptera":
            print("\nHint: " + str(hemipteraHints[pos]))
            pos += 1
            numberOfHints += 1
        if selection == "Hymenoptera":
            print("\nHint: " + str(hymenopteraHints[pos]))
            pos += 1
            numberOfHints += 1
        if selection == "Diptera":
            print("\nHint: " + str(dipteraHints[pos]))
            pos += 1
            numberOfHints += 1
        if selection == "Lepidoptera":
            print("\nHint: " + str(lepidopteraHints[pos]))
            pos += 1
            numberOfHints += 1
        if selection == "Coleoptera":
            print("\nHint: " + str(coleopteraHints[pos]))
            pos += 1
            numberOfHints += 1
        if selection == "Orthoptera":
            print("\nHint: " + str(orthopteraHints[pos]))
            pos += 1
            numberOfHints += 1
        if selection == "Odonata":
            print("\nHint: " + str(odonataHints[pos]))
            pos += 1
            numberOfHints += 1

        #IF statement that stops game if out of hints
        if numberOfHints == 5:
            print("\nOut of hints. Take a guess!\n")
            lastChance = input("Guess: ")
            if lastChance == selection:
                print("\nYou Win! Number of Hints: " + str(numberOfHints))
                break
            else:
                print("\nSorry, you lose.\nThe order was: " + str(selection) + "\nNumber of Hints: " + str(numberOfHints))
                break

        #USER input
        guess = input("\nGuess or New Hint: ")

        #Win if you get the right answer
        if guess == selection:
            print("\nYou Win!\nNumber of Hints: " + str(numberOfHints))
            break
        elif guess == "":
            continue
        else:
            print("\nSorry, you lose.\nThe order was: " + str(selection) + "\nNumber of Hints: " + str(numberOfHints))
            break

    #play again if user inputs "yes",
    playAgain = input("\nDo you want to play again? (Type yes if so) ")
    if playAgain == "yes":
        continue
    else:
        import EntomologyProjectMain
