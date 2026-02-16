
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
    
def board_selection():     #board selection
        r_board=client_socket_2.recv(1024).decode()
        if(r_board=='1'):
            print("player 1 chance to choose the board size ... ")
            board_size=client_socket_2.recv(1024).decode()
            print("player 1 choosen board size : ",board_size)
        elif(r_board=='2'):
            board_size=input("Your turn to enter the Board size : ")
            client_socket_2.send(board_size.encode())
        return board_size

class board:
    def __init__(self,size):
          self.size=size

    def display(self,l):   # display board 
        k=0
        print("\n\t\t","----"*self.size)
        for i in range(0,self.size):
            print("\t\t|",end="")
            for j in range(0,self.size):
                print("",l[i][j],"|",end="")
                k+=1
            print("\n\t\t","----"*self.size)
        print("\n")

    def board_display(self,client_socket_2):    # reciving board converter
        raw_l=client_socket_2.recv(1024).decode()
        l=json.loads(raw_l)
        self.display(l)    
    

client_socket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # player 2 connect to sever
ip_address=input("\n\nEnter the IP ADDRESS of SERVER ! :")
client_socket_2.connect((ip_address, 5000))
client_id='2'
client_socket_2.send(client_id.encode())

try:
    while(1):

        # game start request send to srever

        a=input("\n\nenter 1 to start , 0 to exit : ")
        client_socket_2.send(a.encode())
        print("waiting for player 1 to start ...")
        a=int(a)
        c=int(client_socket_2.recv(1024).decode())
        if(a!=1 and a!=0 and c!=0 and c!=1):
           print("Enter a valid Input")
        else:
           break


    while(a==1 and c==1):

        # board selection

        print("\n\n\t\t\tTIC TAC TOE\n")
        board_size=int(board_selection())
        b2=board(board_size)
        ps2=0
        p1,p2=player(),player()  

    
        # assigning and reciving name of the players

        print("\nwait for player 1 input name...")
        a1=client_socket_2.recv(1024).decode()
        print("player 1 name : ",a1)
        b=input("enter the name :")
        client_socket_2.send(b.encode())
        p1.set_name_and_data(a1,"X")
        p2.set_name_and_data(b,"O")
        b2.board_display(client_socket_2)      # display board


        for i in range((board_size*board_size//2)+1):

            # player 1 position mechanism

            print("player 1 entering position ...")
            b2.board_display(client_socket_2)
            if(client_socket_2.recv(1024).decode()!="No"):
                print(f"\t\tWinner is {p1.get_name()} !\n\n ")       # win check player 1
                break

            # player 2 position mechanism

            if(ps2 < (board_size*board_size)//2):
                while(1):
                    p2_pos=input(f"{p2.get_name()} Enter Your Position (1 - {board_size*board_size}) : ")
                    client_socket_2.send(p2_pos.encode())
                    if(client_socket_2.recv(1024).decode()=="True"):
                        print("The position is already occupied !  or  INVALID position...\n")
                        continue
                    else:
                        break 
                b2.board_display(client_socket_2)
                if(client_socket_2.recv(1024).decode()!="No"):
                    print(f"\t\tWinner is {p2.get_name()} !\n\n")      # win check player 2
                    break
                ps2+=1


        if client_socket_2.recv(1024).decode()=="No":    # draw check 
            print("\t\tThe Match is a TIE ! \n\n")

        # match restart by players choice  

        print("MATCH RESTARTING ...")    
        q=input("enter 1 to start , 0 to exit : ")
        client_socket_2.send(q.encode())
        print("waiting for player 1 to start ...")
        f=(client_socket_2.recv(1024).decode())
        a,c=int(q),int(f)

    if(a!=1 or c!=1):
        print("\n\n\t\tGAME CLOSED (Player 1 or YOU quiet the GAME) ! \n\n")

except:
    print("\n\n\t\tplayer 1 connection was lost ! \n\n")

client_socket_2.close()    
