import random
class snake:
    def __init__(self,size):
        self.size=size 
        self.l=[]
        self.l1=['X']+list('-'*(self.size-1))
        self.l.append(self.l1)
        for i in range(0,self.size-1):
            self.l1=list('-'*self.size)
            self.l.append(self.l1)
        self.hr=0
        self.hc=0
        self.r_row=0
        self.r_column=0
        self.egg=0
        self.body=[(0,0)] 



    def display(self):
        k=0
        for i in range(0,self.size):
            print("\t\t",end="")
            for j in range(0,self.size):
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

        self.body.insert(0,(self.hr,self.hc)) #insert head
        self.l[self.hr][self.hc]="X"

        if len(self.body) > self.egg+1:  #remove tail
            tr,tc = self.body.pop()
            self.l[tr][tc]="-"

        for r,c in self.body[1:]:  #add body
            self.l[r][c]="o" 
   



    def g_food(self):
        while(True):
            self.r_row=random.randint(0,self.size-1)
            self.r_column=random.randint(0,self.size-1) 
            if (self.r_row,self.r_column) in self.body:
                    continue
            else:
                self.l[self.r_row][self.r_column]="V"
                break


    def collision_check(self):
        if (self.hr,self.hc) in self.body[1:]:
            return True
        return False
    

    def food_check(self):
        if(self.r_row==self.hr and self.r_column==self.hc):
            self.egg +=1
            return 1 
        else:
            return 0       
            
          
a=int(input("enter 1 to start Game ,0 to exit :"))
board_size=int(input("\n\t\tEnter the Board Size : "))
p1=snake(board_size) 
while(a==1):
    print("\n\n\t\t SNAKE GAME ! \n\n")
    b_o=0
    c=0
    p1.g_food()
    while(c==0):
        p1.display()
        b=input("enter (WASD) to MOVE :  ")
        if(p1.move(b)==1):
            b_o=1
            break
        c=p1.food_check()
        p1.display()
    if(b_o==1):
        p1=snake(board_size)
        a=int(input("\n\t\tenter 1 to start ,0 to exit :"))
    p1.display()    
import random
class snake:
    def __init__(self,size):
        self.size=size 
        self.l=[]
        self.l1=['X']+list('-'*(self.size-1))
        self.l.append(self.l1)
        for i in range(0,self.size-1):
            self.l1=list('-'*self.size)
            self.l.append(self.l1)
        self.hr=0
        self.hc=0
        self.r_row=0
        self.r_column=0
        self.egg=0
        self.body=[(0,0)] 



    def display(self):
        k=0
        for i in range(0,self.size):
            print("\t\t",end="")
            for j in range(0,self.size):
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

        self.body.insert(0,(self.hr,self.hc)) #insert head
        self.l[self.hr][self.hc]="X"

        if len(self.body) > self.egg+1:  #remove tail
            tr,tc = self.body.pop()
            self.l[tr][tc]="-"

        for r,c in self.body[1:]:  #add body
            self.l[r][c]="o" 
   



    def g_food(self):
        while(True):
            self.r_row=random.randint(0,self.size-1)
            self.r_column=random.randint(0,self.size-1) 
            if (self.r_row,self.r_column) in self.body:
                    continue
            else:
                self.l[self.r_row][self.r_column]="V"
                break


    def collision_check(self):
        if (self.hr < 0 or self.hr > (self.size-1)) or (self.hc < 0 or self.hc > (self.size-1)):
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
            
          
a=int(input("enter 1 to start Game ,0 to exit :"))
board_size=int(input("\n\t\tEnter the Board Size : "))
p1=snake(board_size) 
while(a==1):
    print("\n\n\t\t SNAKE GAME ! \n\n")
    b_o=0
    c=0
    p1.g_food()
    while(c==0):
        p1.display()
        b=input("enter (WASD) to MOVE :  ")
        if(p1.move(b)==1):
            b_o=1
            break
        c=p1.food_check()
        p1.display()
    if(b_o==1):
        p1=snake(board_size)
        a=int(input("\n\t\tenter 1 to start ,0 to exit :"))
    p1.display()    
import random
class snake:
    def __init__(self,size):
        self.size=size 
        self.l=[]
        self.l1=['X']+list('-'*(self.size-1))
        self.l.append(self.l1)
        for i in range(0,self.size-1):
            self.l1=list('-'*self.size)
            self.l.append(self.l1)
        self.hr=0
        self.hc=0
        self.r_row=0
        self.r_column=0
        self.egg=0
        self.body=[(0,0)] 



    def display(self):
        k=0
        for i in range(0,self.size):
            print("\t\t",end="")
            for j in range(0,self.size):
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

        self.body.insert(0,(self.hr,self.hc)) #insert head
        self.l[self.hr][self.hc]="X"

        if len(self.body) > self.egg+1:  #remove tail
            tr,tc = self.body.pop()
            self.l[tr][tc]="-"

        for r,c in self.body[1:]:  #add body
            self.l[r][c]="o" 
   



    def g_food(self):
        while(True):
            self.r_row=random.randint(0,self.size-1)
            self.r_column=random.randint(0,self.size-1) 
            if (self.r_row,self.r_column) in self.body:
                    continue
            else:
                self.l[self.r_row][self.r_column]="V"
                break


    def collision_check(self):
        if (self.hr < 0 or self.hr > (self.size-1)) or (self.hc < 0 or self.hc > (self.size-1)):
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
            
          
a=int(input("enter 1 to start Game ,0 to exit :"))
board_size=int(input("\n\t\tEnter the Board Size : "))
p1=snake(board_size) 
while(a==1):
    print("\n\n\t\t SNAKE GAME ! \n\n")
    b_o=0
    c=0
    p1.g_food()
    while(c==0):
        p1.display()
        b=input("enter (WASD) to MOVE :  ")
        if(p1.move(b)==1):
            b_o=1
            break
        c=p1.food_check()
        p1.display()
    if(b_o==1):
        p1=snake(board_size)
        a=int(input("\n\t\tenter 1 to start ,0 to exit :"))
    p1.display()    
import random
class snake:
    def __init__(self,size):
        self.size=size 
        self.l=[]
        self.l1=['X']+list('-'*(self.size-1))
        self.l.append(self.l1)
        for i in range(0,self.size-1):
            self.l1=list('-'*self.size)
            self.l.append(self.l1)
        self.hr=0
        self.hc=0
        self.r_row=0
        self.r_column=0
        self.egg=0
        self.body=[(0,0)] 



    def display(self):
        k=0
        for i in range(0,self.size):
            print("\t\t",end="")
            for j in range(0,self.size):
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

        self.body.insert(0,(self.hr,self.hc)) #insert head
        self.l[self.hr][self.hc]="X"

        if len(self.body) > self.egg+1:  #remove tail
            tr,tc = self.body.pop()
            self.l[tr][tc]="-"

        for r,c in self.body[1:]:  #add body
            self.l[r][c]="o" 
   



    def g_food(self):
        while(True):
            self.r_row=random.randint(0,self.size-1)
            self.r_column=random.randint(0,self.size-1) 
            if (self.r_row,self.r_column) in self.body:
                    continue
            else:
                self.l[self.r_row][self.r_column]="V"
                break


    def collision_check(self):
        if (self.hr < 0 or self.hr > (self.size-1)) or (self.hc < 0 or self.hc > (self.size-1)):
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
            
          
a=int(input("enter 1 to start Game ,0 to exit :"))
board_size=int(input("\n\t\tEnter the Board Size : "))
p1=snake(board_size) 
while(a==1):
    print("\n\n\t\t SNAKE GAME ! \n\n")
    b_o=0
    c=0
    p1.g_food()
    while(c==0):
        p1.display()
        b=input("enter (WASD) to MOVE :  ")
        if(p1.move(b)==1):
            b_o=1
            break
        c=p1.food_check()
        p1.display()
    if(b_o==1):
        p1=snake(board_size)
        a=int(input("\n\t\tenter 1 to start ,0 to exit :"))
    p1.display()    
