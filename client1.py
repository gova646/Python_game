"""This is the client code. Run this and connect to the server.
 Server contains the game processing logic"""
import socket

from inputs import get_digits_count,get_user_number,get_masked_user_number,get_user_name
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))
#Provide the server address inplace of localhost if running on different systems

print('Welcome to the cows and bulls game!')
# Get a name from the user
player1_name = get_user_name('Player1 Please enter your name')
digits_count = get_digits_count()
player1_user_number = get_masked_user_number(digits_count,'Player1 Please enter your number')

# Send the name to the server
s.send(bytes(player1_name, 'utf-8'))
# s.send(bytes(digits_count, 'utf-8'))
s.send(digits_count.to_bytes(4, byteorder='big'))
s.send(player1_user_number.to_bytes(4, byteorder='big')) 
# s.send(bytes(player1_user_number, 'utf-8'))
print(f"Sent name to server: {player1_name}")

# Receive and print the server's welcome message
response = s.recv(1024).decode()
print(f"Server says: {response}")
game_in_progress = s.recv(1024).decode()
while game_in_progress:
    player1_check_number = get_user_number(digits_count,'Player1 Please enter the number you want to check')
    #s.send(bytes(player1_check_number, 'utf-8'))
    s.send(player1_check_number.to_bytes(4, byteorder='big'))     
    response = s.recv(1024).decode()
    print(f"Server says: {response}")
    game_in_progress = s.recv(1024).decode()
    print(game_in_progress)

response = s.recv(1024).decode()
print(f"Server says: {response}")
# Close the connection
s.close()
