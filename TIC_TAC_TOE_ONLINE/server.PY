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
    


class tictactoe:
    def __init__ (self,size):
        self.size=size 
        self.l=[]
        self.l1=[]
        for i in range(0,self.size):
            self.l1=list('-'*self.size)
            self.l.append(self.l1)
    
    def display(self):  
        k=0
        print("\n\t\t","----"*self.size)
        for i in range(0,self.size):
            print("\t\t|",end="")
            for j in range(0,self.size):
                print("",self.l[i][j],"|",end="")
                k+=1
            print("\n\t\t","----"*self.size)
        print("\n") 
        
    def assign(self,p,pos):
        while(1):
            if (self.l  [(pos-1)//self.size][(pos-1)%self.size]=='-'):
                self.l[(pos-1)//self.size][(pos-1)%self.size]=p.get_data() 
                break
            else:
                print("Position is Already Occupied. Please Enter Another Position:")
                pos=int(input(f"{p.get_name()} Enter Your Position again :"))
                              
    def check(self):
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
            
            
        



client_socket={}
# Create a socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to IP and port
server_socket.bind(("0.0.0.0", 5000))  # "0.0.0.0" = listen on all interfaces

# Start listening (max 5 connections in queue)
server_socket.listen(2)
print("Server listening on port 5000...")

# Accept connection
k=1
while(k<=2):
    client_socket1, addr = server_socket.accept()
    client_socket[k]=client_socket1
    print(addr," is connected !")
    k +=1
    



while(1):
    a=(input("To start game enter 1, To exit 0 : "))
    client_socket[1].send(a.encode())
    client_socket[2].send(a.encode())
    a=int(a)
    if(a!=1 and a!=0):
        print("Enter a valid Input")
    else:
        break


while(a==1):
    print("\n\n\t\t\tTIC TAC TOE\n")
    board_size=(input("Enter the Board Size : "))
    client_socket[1].send(board_size.encode())
    client_socket[2].send(board_size.encode())
    board_size=int(board_size)
    cl=tictactoe(board_size)
    ps2=0
    p1=player()
    p2=player()
    if(int(client_socket[1].recv(1024).decode())==1):
        pass
    if(int(client_socket[2].recv(1024).decode())==2):
        pass
    else:
        temp=client_socket[1]
        client_socket[1]=client_socket[2]
        client_socket[2]=temp    
    



    a1=client_socket[1].recv(1024).decode()
    print("player 1 name : ",a1)
    client_socket[2].send(a1.encode())
    b=client_socket[2].recv(1024).decode()
    print("player 2 name : ",b)
    client_socket[1].send(b.encode())
    p1.set_name_and_data(a1,"X")
    p2.set_name_and_data(b,"O")


    data=json.dumps(cl.l)
    client_socket[1].send(data.encode())
    client_socket[2].send(data.encode())
    cl.display()


    for i in range((board_size*board_size//2)+1):
        print("player 1 ",a1," entering position ...")
        p1_pos=int(client_socket[1].recv(1024).decode())
        cl.assign(p1,int(p1_pos))
        data=json.dumps(cl.l)
        client_socket[1].send(data.encode()) 
        client_socket[2].send(data.encode())
        cl.display()
        client_socket[1].send(cl.check().encode())
        client_socket[2].send(cl.check().encode())
        if(cl.check()!="No"):
            print(f"\t\tWinner is {p1.get_name()} !\n\n ")
            break
        if(ps2 < (board_size*board_size)//2):
            print("player 2 ",b," entering position ...")
            p2_pos=int(client_socket[2].recv(1024).decode())
            cl.assign(p2,p2_pos)
            data=json.dumps(cl.l)
            client_socket[2].send(data.encode())
            client_socket[1].send(data.encode())
            cl.display()
            client_socket[1].send(cl.check().encode())
            client_socket[2].send(cl.check().encode())
            if(cl.check()!="No"):
                print(f"\t\tWinner is {p2.get_name()} !\n\n")
                break
            ps2+=1

            
    client_socket[1].send(cl.check().encode())  
    client_socket[2].send(cl.check().encode())      
    if cl.check()=="No":
        print("\t\tThe Match is a TIE ! \n\n")
    q=input("To start game enter 1, To exit 0 : ")
    client_socket[1].send(q.encode())
    client_socket[2].send(q.encode())
    a=int(q)
