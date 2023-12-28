"""
This is the server code. Contains the game processing logic.
"""
import socket
from inputs import get_digits_count,get_user_number,get_masked_user_number,get_user_name
from cows import get_cows

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind(('localhost', 9999))
# Add the server hosting ip instead of local host for 2 player mode
s.listen(1)
print('Waiting for connections')

while True:
    c, addr = s.accept()
    player1_name = c.recv(1024).decode()
    received_data = c.recv(4)  # Assuming a 32-bit integer
    digits_count = int.from_bytes(received_data, byteorder='big')
    received_data = c.recv(4)
    player1_user_number = int.from_bytes(received_data, byteorder='big')
    print(f'Connected with {addr}, Name: {player1_name} , digits count : {digits_count}')

    # Send a welcome message back to the client
    welcome_message = f"Welcome, {player1_name}! Connected to the server."
    c.send(bytes(welcome_message, 'utf-8'))
    player2_name = get_user_name('Player2 Please enter your name')
    player2_user_number = get_masked_user_number(digits_count,'Player 2 Please enter your number')    
    game_in_progress = 'True'
    c.send(bytes(game_in_progress,'utf-8'))
    while(True):
        print('Now it is '+player1_name+' turn')
        received_data = c.recv(4)
        player1_check_number = int.from_bytes(received_data, byteorder='big')
        #player1_check_number = c.recv(1024).decode()        
        player1_counts = get_cows(str(player2_user_number),str(player1_check_number))
        if player1_counts[0] == digits_count:
            client_message = player1_name+' won. He identified '+ player2_name+' number as ',player1_check_number
            print(client_message)
            client_message = 'You won the game.Great!'            
            winner = player1_name
            game_in_progress = 0
            break
        number_of_cows = f'number of cows are {player1_counts[0]} \n number of bulls are {player1_counts[1]}'        
        c.send(bytes(number_of_cows,'utf-8'))
        #c.send(bytes(number_of_bulls,'utf-8'))

        print('Now it is '+player2_name+' turn')

        player2_check_number = get_user_number(digits_count,'Player2 Please enter the number you want to check')
        player2_counts = get_cows(str(player1_user_number),str(player2_check_number))
        if player2_counts[0] == digits_count:
            print(player2_name+' won. He identified '+player1_name +' number as ',player2_check_number)
            winner = player2_name
            client_message = f'You lost the game.Other player number is {player2_user_number}'
            game_in_progress = 0
            break
        print(game_in_progress)
        c.send(bytes(game_in_progress,'utf-8'))
        print('number of cows are ',player2_counts[0])
        print('number of bulls are ',player2_counts[1])
    c.send(bytes(client_message,'utf-8'))
    print('Winner is '+winner)
    if winner == player2_name:
        print(f'{player2_name} number is {player2_user_number}')
    else:
        print(f'{player1_name} number is {player1_user_number}')
    #print(get_cows(str(user_number),str(check_number)))

    c.close()
