def hangman():    
    Chooseword = input("word: ")
    Lives = 5
    print(int(len(Chooseword))*"_")
    Listword = list(Chooseword)
    Display= list((len(Chooseword))*"_")
    Letterbank = []
    while Lives > 0:
        Guess = input("Guess Letter/Word: ")
        if Guess in  Letterbank:
            print("Already Guessed This")
        else:
            if Guess not in Listword:
                if Guess != Chooseword:
                    Lives = Lives - 1
                    print("You Have", Lives, "Tries Left")
                    if Lives <= 0:
                        print("You Lost")
            
            if Guess == Chooseword:
                print("yay you won")
                break
            elif Guess in Listword:
                Display=list(Display)
                while Guess in Listword:
                    index = int(Listword.index(Guess))
                    Display[index] = Guess
                    Listword[index] = "-"
                DisplayWord=''.join(Display)
                print(DisplayWord)
                if DisplayWord == Chooseword:
                    print("yay you won")  
                    break

            Letterbank.append(Guess)

hangman()
