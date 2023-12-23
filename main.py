from inputs import get_digits_count,get_user_number,get_masked_user_number,get_user_name
from cows import get_cows

def __main__():
    digits_count = get_digits_count()
    player1_name = get_user_name('Player1 Please enter your name')
    player1_user_number = get_masked_user_number(digits_count,'Player1 Please enter your number')
    player2_name = get_user_name('Player2 Please enter your name')
    player2_user_number = get_masked_user_number(digits_count,'Player 2 Please enter your number')
    
    # cows_count = 0
    while(True):
        print('Now it is '+player1_name+' turn')
        player1_check_number = get_user_number(digits_count,'Player1 Please enter the number you want to check')
        player1_counts = get_cows(str(player2_user_number),str(player1_check_number))
        if player1_counts[0] == digits_count:
            print(player1_name+' won. He identified '+ player2_name+' number as ',player1_check_number)
            winner = player1_name
            break
        print('number of cows are ',player1_counts[0])
        print('number of bulls are ',player1_counts[1])

        print('Now it is '+player2_name+' turn')

        player2_check_number = get_user_number(digits_count,'Player2 Please enter the number you want to check')
        player2_counts = get_cows(str(player1_user_number),str(player2_check_number))
        if player2_counts[0] == digits_count:
            print(player2_name+' won. He identified '+player1_name +' number as ',player2_check_number)
            winner = player2_name
            break
        print('number of cows are ',player2_counts[0])
        print('number of bulls are ',player2_counts[1])

    print('Winner is '+winner)
    if winner == player2_name:
        print(player2_name+' number is '+player2_user_number)
    else:
        print(player1_name+' number is '+player1_user_number)
    #print(get_cows(str(user_number),str(check_number)))

__main__()