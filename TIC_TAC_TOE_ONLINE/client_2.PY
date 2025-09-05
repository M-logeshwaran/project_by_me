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
    

class board:
    def __init__(self,size):
          self.size=size

    def display(self,l):  
        k=0
        print("\n\t\t","----"*self.size)
        for i in range(0,self.size):
            print("\t\t|",end="")
            for j in range(0,self.size):
                print("",l[i][j],"|",end="")
                k+=1
            print("\n\t\t","----"*self.size)
        print("\n")

    def board_display(self,client_socket_2):
        raw_l=client_socket_2.recv(1024).decode()
        l=json.loads(raw_l)
        self.display(l)    
    

client_socket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket_2.connect(("10.53.216.184", 5000))
client_id='2'


while(1):
    a=input("\n\nenter 1 to start , 0 to exit : ")
    client_socket_2.send(a.encode())
    print("waiting for player 2 to start ...")
    a=int(a)
    c=int(client_socket_2.recv(1024).decode())
    if(a!=1 and a!=0 and c!=0 and c!=1):
        print("Enter a valid Input")
    else:
        break


while(a==1 and c==1):
    print("\n\n\t\t\tTIC TAC TOE\n")
    board_size=int(client_socket_2.recv(1024).decode())
    b2=board(board_size)
    ps2=0
    p1,p2=player(),player()
    client_socket_2.send(client_id.encode())  


    print("wait for player 1 input name...")
    a1=client_socket_2.recv(1024).decode()
    print("player 1 name : ",a1)
    b=input("enter the name :")
    client_socket_2.send(b.encode())
    p1.set_name_and_data(a1,"X")
    p2.set_name_and_data(b,"O")
    b2.board_display(client_socket_2)


    for i in range((board_size*board_size//2)+1):
        print("player 1 entering position ...")
        b2.board_display(client_socket_2)
        if(client_socket_2.recv(1024).decode()!="No"):
            print(f"\t\tWinner is {p1.get_name()} !\n\n ")
            break
        if(ps2 < (board_size*board_size)//2):
            while(1):
                p2_pos=input(f"{p2.get_name()} Enter Your Position : ")
                client_socket_2.send(p2_pos.encode())
                if(client_socket_2.recv(1024).decode()=="True"):
                    print("The position is already occupied !  or  INVALID position...\n")
                    continue
                else:
                    break 
            b2.board_display(client_socket_2)
            if(client_socket_2.recv(1024).decode()!="No"):
                print(f"\t\tWinner is {p2.get_name()} !\n\n")
                break
            ps2+=1


    if client_socket_2.recv(1024).decode()=="No":
        print("\t\tThe Match is a TIE ! \n\n")
    print("MATCH RESTARTING ...")    
    q=input("enter 1 to start , 0 to exit : ")
    client_socket_2.send(q.encode())
    print("waiting for player 1 to start ...")
    f=(client_socket_2.recv(1024).decode())
    a,c=int(q),int(f)


client_socket_2.close()    
