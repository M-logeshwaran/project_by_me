import random
class snake:
    def __init__(self):
        self.l = [["X","-","-","-","-","-"],
                  ["-","-","-","-","-","-"],
                  ["-","-","-","-","-","-"],
                  ["-","-","-","-","-","-"],
                  ["-","-","-","-","-","-"],
                  ["-","-","-","-","-","-"]]
        self.hr=0
        self.hc=0
        self.r_row=0
        self.r_column=0
        self.egg=0
        self.body=[(0,0)]


    def full(self,k8=6):    # box full logic
        c=0
        for i in range(k8):
            for j in range(k8):
                if(self.l[i][j] == '-'):
                    c=1    
                    break
        if(c==0):
            return 1
        else:
            return 0       


    
    def display(self,k8=6):
        k=0
        for i in range(0,k8):
            print("\t\t",end="")
            for j in range(0,k8):
                print(self.l[i][j],"",end=" ")
                k+=1
            print("\n") 
        print("COUNT :",self.egg)       
        print("\n")



    def move(self,action):
        self.l[self.hr][self.hc]="-"

        if(action in ("W","w")):
            self.hr -= 1
        elif(action in ("S","s")):
            self.hr +=1
        elif(action in ("D","d")):  
            self.hc +=1
        elif(action in ("a","A")):  
            self.hc -=1 

        if self.collision_check():
            print("\n\n\t\tGAME OVER! Snake collided. !\n\n")
            return 1

        self.body.insert(0,(self.hr,self.hc))
        self.l[self.hr][self.hc]="X"

        if len(self.body) > self.egg+1:
            tr,tc = self.body.pop()
            self.l[tr][tc]="-"

        for r,c in self.body[1:]:
            self.l[r][c]="o" 
   



    def g_food(self):
        while(True):
            self.r_row=random.randint(0,5)
            self.r_column=random.randint(0,5) 
            if (self.r_row,self.r_column) in self.body:
                    continue
            else:
                self.l[self.r_row][self.r_column]="V"
                break


    def collision_check(self):
        if (self.hr < 0 or self.hr > 5) or (self.hc < 0 or self.hc > 5):
            return True
        if (self.hr,self.hc) in self.body[1:]:
            return True
        return False
    

    def food_check(self):
        if(self.r_row==self.hr and self.r_column==self.hc):
            self.egg +=1
            return 1 
        else:
            return 0       
            
          
a=input("\nenter 1 to start Game ,0 to exit :")
p1=snake() 
while(a=='1'):
    print("\n\n\t\t SNAKE GAME ! \n\n")
    b_o=0
    c=0
    p1.g_food()
    while(c==0):
        p1.display()
        while(1):
            b=input("enter (WASD) to MOVE :  ")
            if(b not in ('w','W','s','S','A','a','d','D')):
                print("\n\t\tYou entered Invalid input ! Enter again ! \n")
                continue
            else:
                break
        if(p1.move(b)==1):
            b_o=1
            break
        c=p1.food_check()
        p1.display()
    if(b_o==1 or p1.full()==1):
        if(p1.full()==1):
            print("\n\t\tYOU WON THE GAME ! ")
        p1=snake()
        a=input("\nenter 1 to start ,0 to exit :")
    else:    
       p1.display()  
print("\n\t\tTHE GAME CLOSED ! ")         

