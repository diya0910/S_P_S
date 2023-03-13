def logic():
    import random
# Rock Paper Scissors Game
    def game(comp,you):
        # if two values are equal, declare a tie!
        if comp == you:
            return None

        # Check for all possibilities when computer chose 'r'
        elif comp == 'Rock':
            if you == 'Scissors':
                return False
            elif you == 'Paper':
                return True
        # Check for all possibilities when computer chose 'p'
        elif comp == 'Paper':
            if you == 'Rock':
                return False
            elif you == 'Scissors':
                return True
        # Check for all possibilities when computer chose 's'
        elif comp == 'Scissors':
            if you == 'Paper':
                return False
            elif you == 'Rock':
                return True
    # Computer's turn
    print("Computer's Turn: Rock(R) Paper(P) or Scissors(S)?")
    randomNum = random.randint(1,3)
    if randomNum == 1:
        comp = 'Rock'
    elif randomNum == 2:
        comp = 'Paper'
    elif randomNum == 3:
        comp = 'Scissors'
    print("Computer has Chosen")

    # Player's turn
    you = input("Player's Turn: Rock(R) Paper(P) or Scissors(S)? ")
    you = you.lower()
    if you == 'r':
        you = you.replace("r","Rock")
    if you == 's':
        you = you.replace("s","Scissors")
    if you == 'p':
        you = you.replace("p","Paper") 
    a = game(comp,you)

    # Result
    print(f"Computer chose {comp}.")
    print(f"You chose {you}.")

    if a == None:
        print("The game is a tie!")
    elif a:
        print("Congratulations!\nYou Win!")
    else:
        print("You Lose!\nTry Again!")
logic()
while True:
    again = input("Play again...?\nYes(Y) or No(N)...?")
    again = again.lower()
    if again == 'y':
        logic()
    else:
        exit()