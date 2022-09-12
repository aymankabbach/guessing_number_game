def determine_wanted_number():
    import random 
    random_number=random.randint(1,100)
    return random_number
def showing_modes(modes):
    x=0
    for mode in modes:
        print(x+1,mode)
        x=x+1
def read_player_choice():
    user_input=int(input("choose a dificulty\n"))
    return user_input
def check_player_input(user_input,modes):
    if user_input<1 or user_input>len(modes):
        print("wrong input, try something else")
        return True
    else:
        return False
def get_player_choice(modes):
    wrong_input=True
    while wrong_input==True:
        try:
            user_input=read_player_choice()
        except ValueError:
            print("wrong input, try something else")
            wrong_input==True
        else:
            wrong_input=check_player_input(user_input,modes)
    return modes[user_input-1]
def determine_attempts(choosen_mode,modes):
    if choosen_mode==modes[0]:
        return 10
    if choosen_mode==modes[1]:
        return 5
def read_guessed_number():
    user_input=int(input("guess a number between 1 and 100\n"))
    return user_input
def check_input(user_input):
    if user_input<1 or user_input>100:
        print("wrong input, try something else")
        return True
    else:
        return False
def get_guessed_number():
    wrong_input=True
    while wrong_input==True:
        try:
            user_input=read_guessed_number()
        except ValueError:
            print("wrong input, try something else")
            wrong_input==True
        else:
            wrong_input=check_input(user_input)
    return user_input
def check_win(player_number,wanted_number):
    if player_number==wanted_number:
        return True
    else:
        return False
def update_attempts_left(player_number,wanted_number,attempts):
    if player_number>wanted_number:
        print("too high") 
    elif player_number<wanted_number:
        print("too low")
    attempts=attempts-1
    if attempts>0:
        print(f"you still have {attempts} attempts")
    return attempts
def gameOver(wanted_number):
        print(f"Game Over\nthe number was {wanted_number}")
def start_Game():
    winner=False
    print("welcome to the Number Guessing Game! \nyou need to guess a number between 1 and 100 \nyou have 5 attempts in hard level \nand 10 in easy level")
    wanted_number=determine_wanted_number()
    modes=["easy","hard"]
    showing_modes(modes)
    choosen_mode=get_player_choice(modes)
    attempts=determine_attempts(choosen_mode,modes)
    while attempts>0 and winner==False:
        player_number=get_guessed_number()
        winner=check_win(player_number,wanted_number)
        if winner==False:
            attempts=update_attempts_left(player_number,wanted_number,attempts)
    if winner==True:
        print("you win")
    if attempts==0:
        gameOver(wanted_number)    
start_Game()



