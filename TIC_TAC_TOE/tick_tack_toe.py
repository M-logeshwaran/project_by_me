class player:
    def __init__(self):
        self.__name=""
        self.data=""
    def set_name_and_data(self,name,data):
        self.data=data
        self.__name=name
    def get_name(self):
        return self.__name
    def get_data(self):
        return self.data




class tictactoe:
    def __init__ (self,k8): 
        self.l=[]
        self.l1=[]
        for i in range(0,k8):
            self.l1=list('-'*k8)
            self.l.append(self.l1)
    
    def display(self,k8):
        k=0
        print("\n\t\t","----"*k8)
        for i in range(0,k8):
            print("\t\t|",end="")
            for j in range(0,k8):
                print("",self.l[i][j],"|",end="")
                k+=1
            print("\n\t\t","----"*k8)
        print("\n") 
        
    def assign(self,p,pos):
        self.l[(pos-1)//k8][(pos-1)%k8]=p.data 

    def check(self,k8):
        while True:
            X,O=0,0
            for i in self.l:   #[[],[],[],[],[]]  row wise
                s=''
                for j in i:
                    s+=j
                if(s=='X'*k8):
                    X=1
                    return 'X'
                    break
                elif(s=='O'*k8):
                    O=1
                    return 'O'
                    break


            s1=''
            for j in range(0,k8):    #[[],[],[],[],[]]  column wise
                s1=''
                for i in self.l: 
                    s1+=i[j]
                if(s1=='X'*k8):
                    X=1
                    return 'X'
                    break
                elif(s1=='O'*k8):
                    O=1
                    return 'O'
                    break    



            s2=''
            for i in range(0,k8):   #[[],[],[],[],[]]  diagnol from L-R wise
                 s2+=self.l[i][i]
            if(s2=='X'*k8):
                X=1
                return 'X'
                break
            elif(s2=='O'*k8):
                O=1
                return 'O'
                break


            s3=''
            r,c=0,(k8-1)
            for i in range(0,k8):   #[[],[],[],[],[]]  diagnol from R-L wise
                 s3+=self.l[r][c]
                 r=r+1
                 c=c-1
            if(s3=='X'*k8):
                return 'X'
                break
            elif(s3=='O'*k8):
                return 'O'
                break

            if(X==0):
                return "No"
                break
            elif(O==0):
                return "No"
                break





while(1):
    a=int(input("To start game enter 1, To exit 0 : "))
    if(a!=1 and a!=0):
        print("Enter a valid Input")
    else:break
while(a==1):
    print("\n\n\t\t\tTICK TACK TOE\n")
    k8=int(input("\nEnter the Grid Size : "))
    cl=tictactoe(k8)
    cl.display(k8)
    t=k8*k8
    ps2=0
    p1=player()
    p2=player()
    a=input("\n\nEnter Player 1 (X) Name : ")
    b=input("Enter Player 2 (O) Name : ")
    p1.set_name_and_data(a,"X")
    p2.set_name_and_data(b,"O")
    cl.display(k8)
    for i in range((k8*k8//2)+1):
        p1_pos=int(input(f"Player 1 (X) Enter Your Position (1-{t}) : "))
        cl.assign(p1,p1_pos)
        cl.display(k8)
        if(cl.check(k8)!="No"):
            print(f"\a\t\tWinner is {p1.get_name()} ! \n\n")
            break
        if(ps2 < (k8*k8)//2):
            p2_pos=int(input(f"Player 2 (O) Enter Your Position (1-{t}) : "))
            cl.assign(p2,p2_pos)
            cl.display(k8)
            if(cl.check(k8)!="No"):
                print(f"\a\t\tWinner is {p2.get_name()} ! \n\n")
                break
            ps2+=1
    if cl.check(k8)=="No":
        print("\a\t\tThe Match is a TIE ! \n\n")
    a=int(input("To start game enter 1, To exit 0 : "))





    


