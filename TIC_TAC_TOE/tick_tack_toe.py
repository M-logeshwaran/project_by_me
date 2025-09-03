class player:
    def __init__(self):
        self.__name=""
        self.data=""
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
            
            

    def reset(self):
        self.l=[]
        self.l1=[] 
        for i in range(0,self.size):
            self.l1=list('-'*self.size)
            self.l.append(self.l1)
        






while(1):
    a=int(input("To start game enter 1, To exit 0 : "))
    if(a!=1 and a!=0):
        print("Enter a valid Input")
    else:
        break
while(a==1):
    print("\n\n\t\t\tTICK TACK TOE\n")
    board_size=int(input("Enter the Board Size : "))
    cl=tictactoe(board_size)
    cl.reset()
    ps2=0
    p1=player()
    p2=player()
    a=input("Enter Player 1 Name : ")
    b=input("Enter Player 2 Name : ")
    p1.set_name_and_data(a,"X")
    p2.set_name_and_data(b,"O")
    cl.display()
    for i in range((board_size*board_size//2)+1):
        p1_pos=int(input(f"{p1.get_name()} Enter Your Position (1-{board_size*board_size}) : "))
        cl.assign(p1,p1_pos)
        cl.display()
        if(cl.check()!="No"):
            print(f"\t\tWinner is {p1.get_name()} !\n\n ")
            break
        if(ps2 < (board_size*board_size)//2):
            p2_pos=int(input(f"{p2.get_name()} Enter Your Position (1-{board_size*board_size}) : "))
            cl.assign(p2,p2_pos)
            cl.display()
            if(cl.check()!="No"):
                print(f"\t\tWinner is {p2.get_name()} !\n\n")
                break
            ps2+=1
    if cl.check()=="No":
        print("\t\tThe Match is a TIE ! \n\n")
    a=int(input("To start game enter 1, To exit 0 : "))
