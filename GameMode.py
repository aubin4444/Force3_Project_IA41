def start():
    choice = 0
    level_choice = ["1", "2", "3"]
    print("What mode of game do you want ?")
    print("-(1): Player VS Player\n-(2): Player VS IA\n-(3): IA VS IA")
    while choice not in level_choice:
        choice = input()

def next_round(board, player):

    if player.circletoken_id <= 2:
        answer = int(input("What do you want to do for the next round?\n"
                    "-(1) : Add circle token\n"
                    "-(2) : Move circle token\n"
                    "-(3) : Move square token\n"))
        while answer not in {1, 2, 3}:
            answer = int(input())
    else :
        answer = int(input("What do you want to do for the next round?\n"
                           "-(2) : Move circle token\n"
                           "-(3) : Move square token\n"))
        while answer not in {2, 3}:
            answer = int(input())
    if answer == 1:
        check = 0
        print("You are going to add a circle token on the playing area :\n")
        while check == 0:
            coordinate_x = int(input("Choose the targeted x coordinate among (0,1,2) :\n"))
            while coordinate_x not in {0, 1, 2}:
                coordinate_x = int(input())

            coordinate_y = int(input("Choose the targeted y coordinate among (0,1,2) :\n"))
            while coordinate_y not in {0, 1, 2}:
                coordinate_y = int(input())
            check = board.addCircleToken(coordinate_x,coordinate_y,player)
    elif answer == 2:
        print("You are going to move a circle token :\n")
        coordinate_x = int(input("Choose the targeted x coordinate among (0,1,2) :\n"))
        while coordinate_x not in {0, 1, 2}:
            coordinate_x = int(input())
        coordinate_y = int(input("Choose the targeted y coordinate among (0,1,2) :\n"))
        while coordinate_y not in {0, 1, 2}:
            coordinate_y = int(input())
        #Display the list of the available token_id
        print("Which circle token do you want to move :\n")
        if len(player.circletoken) == 3:
            t0, t1, t2 = player.circletoken
            circletoken = int(input("-The first : " + str(t0.token_id) + "\n-The second : " + str(t1.token_id) + "\n-The third : " + str(t2.token_id) + "\n"))
        if len(player.circletoken) == 2:
            t0, t1 = player.circletoken
            circletoken = int(input("-The first : " + str(t0.token_id) + "\n-The second : " + str(t1.token_id) + "\n"))
        #If there are just one circle token
        if len(player.circletoken) == 1:
            circletoken = 0

        while circletoken not in {0, 1, 2}:
            circletoken = input()
        board.moveCircleToken(coordinate_x,coordinate_y,player,circletoken)
    else:
        print("You are going to move a square token :\n")
        coordinate_x = int(input("Choose the x coordinate of the token to move among (0,1,2) :\n"))
        while coordinate_x not in {0, 1, 2}:
            coordinate_x = int(input())
        coordinate_y = int(input("Choose the y coordinate of the token to move among (0,1,2) :\n"))
        while coordinate_y not in {0, 1, 2}:
            coordinate_y = int(input())
        board.moveSquareToken(board.gamearea[coordinate_x][coordinate_y])