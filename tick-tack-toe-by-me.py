import random

def num_board():
  dash=[ str(i) for i in range(1,10)]
  board=[ dash[(i*3):(i*3)+3] for i in range(3)]
  for elem in board:
    print(("|" + "|".join(elem) + "|"))

#avail_moves=[1,2,3,4,5,6,7,8,9]

def winner(ip,check):
    #checking for rows
    row_index = (ip-1)//3
    row= board[row_index]
    if all(check == elem for elem in row):
        print("winner is: ",check) 
        return 1
    #cheking for colm   
    col_index = (ip-1)%3
    col= [board[i][col_index] for i in range (3)]
    if all(check == elem for elem in col):
        print("winner is: ",check)
        return 1
    #check for digonals
    if (ip%2)!=0:
        dig1=[board[i][i] for i in range(3)]
        if all(check == elem for elem in dig1):
            print("winner is: ",check)
            return 1
        dig2=[board[i][3-i-1] for i in range(3)]
        if all(check == elem for elem in dig2):
            print("winner is: ",check) 
            return 1   
        
def user(user_choice):
    global won
    user_ip=int(input("you chose: "))
    while(user_ip in played_moves):
     print("Move is allready used ")
     user_ip=int(input("you choce: "))
    played_moves.append(user_ip)
    row = (user_ip-1)//3
    col = (user_ip-1)%3
    board[row][col]=user_choice
    won=winner(user_ip,user_choice)

def comp(comp_choice):
    global won
    comp_ip=random.randint(1,9)
    while (comp_ip in played_moves):
        comp_ip=random.randint(1,9)
    played_moves.append(comp_ip)
    print("comp choe: ", comp_ip)
    row = (comp_ip-1)//3
    col = (comp_ip-1)%3
    board[row][col]=comp_choice
    won=winner(comp_ip,comp_choice)

won=0
moves=["X","O"]
user_choice=random.choice(moves)
moves.remove(user_choice)
compo_choice=moves[0]
print("You will use: ",user_choice)
print("comp will use: ",moves[0])

played_moves=[]        
num_board()
dash=[" " for i in range(9)]
board=[ dash[(i*3):(i*3)+3] for i in range(3)]

while (any(" " in value for value in board)) and won!=1: 
    if len(played_moves)!=9 and won!=1:
        user(user_choice)
        for elem in board:
            print(("|" + "|".join(elem) + "|"))
            
    if len (played_moves)!=9 and won!=1:
        comp(moves[0])
        for elem in board:
            print(("|" + "|".join(elem) + "|"))
                   
#for elem in board:
#    print(("|" + "|".join(elem) + "|"))
print("Game_over")
