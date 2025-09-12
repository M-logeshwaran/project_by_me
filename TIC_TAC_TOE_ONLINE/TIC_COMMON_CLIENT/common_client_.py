
import socket
import json
  

class player:
    def __init__(self): 
        self.__name=""
        self.__data=""
    def set_name_and_data(self,name,data):
        self.__data=data
        self.__name=name
    def get_name(self):
        return self.__name
    def get_data(self):
        return self.__data
    
def board_selection(player_id):      # board selection
        r_board=client_socket.recv(1024).decode()
        if(player_id =='1'):
            if(r_board == '1'):
                board_size=input("Your turn to enter the Board size : ")
                client_socket.send(board_size.encode())
            elif(r_board =='2'):
                print("player 2 chance to choose the board size ... ")
                board_size=client_socket.recv(1024).decode()
                print("player 2 choosen board size : ",board_size)
        elif(player_id == '2'):
            if(r_board=='1'):
                print("player 1 chance to choose the board size ... ")
                board_size=client_socket.recv(1024).decode()
                print("player 1 choosen board size : ",board_size)
            elif(r_board=='2'):
                board_size=input("Your turn to enter the Board size : ")
                client_socket.send(board_size.encode())       
        return board_size

class board:
    def __init__(self,size):
        self.size=size

    def display(self,l):      # display board
        k=0
        print("\n\t\t","----"*self.size)
        for i in range(0,self.size):
            print("\t\t|",end="")
            for j in range(0,self.size):
                print("",l[i][j],"|",end="")
                k+=1
            print("\n\t\t","----"*self.size)
        print("\n")

    def board_display(self,client_socket):     # reciving board converter
        raw_l=client_socket.recv(1024).decode()
        l=json.loads(raw_l)
        self.display(l)    

def your_turn_logic(board_size,p):
        while(1):
            p_pos=input(f"{p.get_name()} Enter Your Position (1 - {board_size*board_size}) : ")
            client_socket.send(p_pos.encode())
            if(client_socket.recv(1024).decode()=="True"):
                print("The position is already occupied !  or  INVALID position ...\n")
                continue
            else:
                break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # player 1 connect to server
ip_address=input("\n\nEnter the IP ADDRESS of SERVER ! :")
client_socket.connect((ip_address, 5000))
player_id=client_socket.recv(1024).decode()

try :
    while(1):

     # game start request send to srever

        a=input("\n\nenter 1 to start , 0 to exit : ") 
        client_socket.send(a.encode())
        if(player_id=='1'):
            print("waiting for player 2 to start ...")
        else:
            print("waiting for player 1 to start ...")    
        a=int(a)
        c=int(client_socket.recv(1024).decode())
        if(a!=1 and a!=0 and c!=0 and a!=0):
             print("Enter a valid Input")
        else:
            break


    while(a==1 and c==1):

        # board selection

        print("\n\n\t\t\t----- TIC TAC TOE -----\n")
        print("\n\t\t\tYOUR PLAYER "+player_id+" !\n")
        board_size=int(board_selection(player_id))
        b1=board(board_size)
        ps2=0
        p1,p2=player(),player()


        # assigning and reciving name of the players

        a=input("enter the name :")
        client_socket.send(a.encode())
        if(player_id=='1'):
            print("wait for player 2 input name...")
            b=client_socket.recv(1024).decode()
            print("player 2 name : ",b)
            p1.set_name_and_data(a,"X")
            p2.set_name_and_data(b,"O")
        else:
            print("wait for player 1 input name...")   
            b=client_socket.recv(1024).decode()
            print("player 1 name : ",b) 
            p1.set_name_and_data(b,"O")
            p2.set_name_and_data(a,"X")
        b1.board_display(client_socket)      # display board


        for i in range((board_size*board_size//2)+1):

            # player 1 position mechanism
            if(player_id=='1'):
                your_turn_logic(board_size,p1)                       
                b1.board_display(client_socket)
                if(client_socket.recv(1024).decode()!="No"):
                    print(f"\t\tWinner is {p1.get_name()} !\n\n ")     # win check player 1
                    break


                if(ps2 < (board_size*board_size)//2):
                    print("player 2 entering position ...")
                    b1.board_display(client_socket)
                    if(client_socket.recv(1024).decode()!="No"):
                        print(f"\t\tWinner is {p2.get_name()} !\n\n")    # win check player 2
                        break
                    ps2+=1
                    
            # player 2 position mechanism
            elif(player_id=='2'):   
                print("player 1 entering position ...")
                b1.board_display(client_socket)
                if(client_socket.recv(1024).decode()!="No"):
                    print(f"\t\tWinner is {p1.get_name()} !\n\n ")       # win check player 1
                    break


                if(ps2 < (board_size*board_size)//2):
                    your_turn_logic(board_size,p2)  
                    b1.board_display(client_socket)
                    if(client_socket.recv(1024).decode()!="No"):
                        print(f"\t\tWinner is {p2.get_name()} !\n\n")      # win check player 2
                        break
                    ps2+=1



        if client_socket.recv(1024).decode()=="No":      # draw check
            print("\t\tThe Match is a TIE ! \n\n")

        # match restart by players choice

        print("MATCH RESTARTING ...")    
        q=input("enter 1 to start , 0 to exit : ")
        client_socket.send(q.encode())
        if(player_id=='2'):
            print("waiting for player 1 to start ...")
        else:
            print("waiting for player 2 to start ... ")    
        f=(client_socket.recv(1024).decode())
        a,c=int(q),int(f)
          

    if(a!=1 or c!=1):
        if(player_id=='1'):
            print("\n\n\t\tGAME CLOSED (Player 2 or YOU quiet the GAME) ! \n\n")
        else:
            print("\n\n\t\tGAME CLOSED (Player 1 or YOU quiet the GAME) ! \n\n")    

except :
    if(player_id=='1'):
        print("\n\n\t\t Player 2 connection was lost ! \n\n")  
    else:
        print("\n\n\t\t Player 1 connevtion was lost ! \n\n")    
    
client_socket.close()       
