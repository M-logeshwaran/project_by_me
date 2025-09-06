import socket
import json
import random
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
    


class tictactoe:
    def __init__ (self,size):
        self.size=size 
        self.l=[]
        self.l1=[]
        for i in range(0,self.size):
            self.l1=list('-'*self.size)
            self.l.append(self.l1)
    
    def display(self):         # board display
        k=0
        print("\n\t\t","----"*self.size)
        for i in range(0,self.size):
            print("\t\t|",end="")
            for j in range(0,self.size):
                print("",self.l[i][j],"|",end="")
                k+=1
            print("\n\t\t","----"*self.size)
        print("\n") 
        
    def assign(self,p,pos):        # assign in board or update board
            if ((pos <= (self.size*self.size)) and self.l  [(pos-1)//self.size][(pos-1)%self.size]=='-'):
                self.l[(pos-1)//self.size][(pos-1)%self.size]=p.get_data() 
                return True
            else:
                return False
            
    def send_board_clients(self):
        data=json.dumps(self.l)
        client_socket[1].send(data.encode())
        client_socket[2].send(data.encode())  
        
        
    def send_check_clients(self):
        client_socket[1].send(self.check().encode())  
        client_socket[2].send(self.check().encode())    
                 
    def send_assign_recive(self,p,socket_id):    # assign value according to player 1 or 2
        while(1):
            pos=(client_socket[socket_id].recv(1024).decode())
            if(pos.isdigit()==False or self.assign(p,int(pos))==False):
                client_socket[socket_id].send("True".encode())
                continue
            else:
                client_socket[socket_id].send("False".encode())
                break
                              
    def check(self):          # checking mechanism
        while True:
            X,O=0,0
            for i in self.l:   #[[],[],[],[],[]]  row wise
                s=''
                for j in i:
                    s+=j
                if(s=='X'*self.size):
                    X=1
                    return 'X'
                elif(s=='O'*self.size):
                    O=1
                    return 'O'



            s1=''
            for j in range(0,self.size):    #[[],[],[],[],[]]  column wise
                s1=''
                for i in self.l: 
                    s1+=i[j]
                if(s1=='X'*self.size):
                    X=1
                    return 'X'
                elif(s1=='O'*self.size):
                    O=1
                    return 'O'  



            s2=''
            for i in range(0,self.size):   #[[],[],[],[],[]]  diagnol from L-R wise
                 s2+=self.l[i][i]
            if(s2=='X'*self.size):
                X=1
                return 'X'
            elif(s2=='O'*self.size):
                O=1
                return 'O'
            


            s3=''
            r,c=0,(self.size-1)
            for i in range(0,self.size):   #[[],[],[],[],[]]  diagnol from R-L wise
                 s3+=self.l[r][c]
                 r=r+1
                 c=c-1
            if(s3=='X'*self.size):
                return 'X'
            elif(s3=='O'*self.size):
                return 'O'

            if(X==0):
                return "No"
            elif(O==0):
                return "No"
            
def board_selection():                     # Board selection randomly
        r_board=str(random.randint(1,2))
        client_socket[1].send(r_board.encode())
        client_socket[2].send(r_board.encode())
        if(r_board=='1'):
            board_size=client_socket[1].recv(1024).decode()
            client_socket[2].send(board_size.encode())
            print("player 1 choose board size : ",board_size)
        elif(r_board=='2'):
            board_size=client_socket[2].recv(1024).decode()
            client_socket[1].send(board_size.encode()) 
            print("player 2 choose board size : ",board_size) 
        return board_size            
        



client_socket={}                   # client socket dictinory

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # connect client and store their socket in dictionary
server_socket.bind(("0.0.0.0", 5000)) 
server_socket.listen(2)
print("Server listening on port 5000...")
k=1
while(k<=2):
    client_socket1, addr = server_socket.accept()
    client_socket[k]=client_socket1
    print(addr," is connected !")
    k +=1
    


if(int(client_socket[1].recv(1024).decode())==1):                    # rearranging the client socket by their client_id
        pass
if(int(client_socket[2].recv(1024).decode())==2):
        pass
else:
    temp=client_socket[1]
    client_socket[1]=client_socket[2]
    client_socket[2]=temp

try :
    while(1):

        # analysing the starting option  mechanism of game by players

        print("\n\nWaiting for players to start game ... ")
        a,c=(client_socket[1].recv(1024).decode()),(client_socket[2].recv(1024).decode())
        if(a=="1"):
            print("player 1 Ready to play ! ...")
        else:
            print("player 1 quit the game ! ...")
        if(c=="1"):
            print("player 2 Ready to play ! ...")
        else:
            print("player 2 quit the game ! ...")        
        client_socket[1].send(c.encode())
        client_socket[2].send(a.encode())
        a=int(a)
        c=int(c)
        if(a!=1 and a!=0 and c!=1 and c!=0):
            print("Enter a valid Input")
        else:
            break


    while(a==1 and c==1):

        # Board size selection by players randomly

        print("\n\n\t\t\tTIC TAC TOE\n")
        board_size=board_selection()
        board_size=int(board_size)
        cl=tictactoe(board_size)
        ps2=0   

        # assigning player 1 and player 2 name and storing name in player class

        p1=player()
        p2=player()
        print("\n\nwaiting for players to enter the name ...")
        a1=client_socket[1].recv(1024).decode()
        print("player 1 name : ",a1)
        client_socket[2].send(a1.encode())
        b=client_socket[2].recv(1024).decode()
        print("player 2 name : ",b)
        client_socket[1].send(b.encode())
        p1.set_name_and_data(a1,"X")
        p2.set_name_and_data(b,"O")

        cl.send_board_clients()
        cl.display()


        for i in range((board_size*board_size//2)+1):

            # assigning position of player 1 and updating boards and send to the both players

            print("player 1 ",a1," entering position ...")
            cl.send_assign_recive(p1,1)
            cl.send_board_clients()
            cl.display()
            cl.send_check_clients()
            if(cl.check()!="No"):
                print(f"\t\tWinner is {p1.get_name()} !\n\n ")   # win check player 1
                break
        
            # assigning position of player 2 and updating boards and send to the both players

            if(ps2 < (board_size*board_size)//2):
                print("player 2 ",b," entering position ...")
                cl.send_assign_recive(p2,2)
                cl.send_board_clients()
                cl.display()
                cl.send_check_clients() 
                if(cl.check()!="No"):
                    print(f"\t\tWinner is {p2.get_name()} !\n\n")   # win check of player 2
                    break
                ps2+=1

            
        cl.send_check_clients()     
        if cl.check()=="No":           # draw check 
            print("\t\tThe Match is a TIE ! \n\n")

        # match restart by players choice 

        q,f=(client_socket[1].recv(1024).decode()),(client_socket[2].recv(1024).decode())
        client_socket[1].send(f.encode())
        client_socket[2].send(q.encode())
        if(q=='1' and f=='1'):
            a,c=int(q),int(f)
        else:
            break

    print("\n\t\tThe players has been quiet the game !\n\n")

except:
    print("\n\n\t\t Players connections was lost ! \n\n")    

server_socket.close()      
