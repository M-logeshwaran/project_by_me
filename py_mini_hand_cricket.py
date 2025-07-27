import random as r

def h_1st():
    scoreh,scorer=0,0
    print("\n---------------------------------------------------------------------------------------")
    print('\n\t\t >>> YOU WON THE TOSS :')
    h_ebc=input('\n\t\t* Enter your choice [ BAT OR BOWL ] : ')
    if(h_ebc=='BAT'):
        scoreh=h_bat(scorer,'min')
        print('\n\t\t >>> YOUR SCORE :',scoreh)
        print('\n\t\t >>> MY TARGET :',scoreh+1)
        scorer=h_bowl(scoreh,'max')
        print('\n\t\t >>> MY SCORE :',scorer)
        return scoreh,scorer
    elif(h_ebc=='BOWL'):
        scorer=h_bowl(scoreh,'min')
        print('\n\t\t >>> MY SCORE :',scorer)
        print('\n\t\t >>> YOUR TARGET :',scorer+1)
        scoreh=h_bat(scorer,'max')
        print('\n\t\t >>> YOUR SCORE :',scoreh)
        return scoreh,scorer

def r_1st():
    scoreh,scorer=0,0
    r_bb=r.randint(2,3)
    print("\n---------------------------------------------------------------------------------------")
    print('\n\t\t >>> I WON THE TOSS :')
    print('\n\t\t* MY choice [ BAT OR BOWL ] : ',l[r_bb])
    if(l[r_bb]=='BOWL'):
        scoreh=h_bat(scorer,'min')
        print('\n\t\t >>> YOUR SCORE :',scoreh)
        print('\n\t\t >>> MY TARGET :',scoreh+1)
        scorer=h_bowl(scoreh,'max')
        print('\n\t\t >>> MY SCORE :',scorer)
        return scoreh,scorer
    elif(l[r_bb]=='BAT'):
        scorer=h_bowl(scoreh,'min')
        print('\n\t\t >>> MY SCORE :',scorer)
        print('\n\t\t >>> YOUR TARGET :',scorer+1)
        scoreh=h_bat(scorer,'max')
        print('\n\t\t >>> YOUR SCORE :',scoreh)
        return scoreh,scorer

                    
def h_bat(scorer,s):
    score=0
    while(True):
        r_bowl=r.randint(0,6)
        try:
            h_bat=int(input('\n\t\t* Enter your NUM SCORE [ 0 TO 6 ] for BAT : '))
        except:
            print('\n\t\t ERROR ! INT TYPE only !')
        print('\n\t\t* MY NUM SCORE [ 0 TO 6 ] for BOWL : ',r_bowl)
        if(r_bowl!=h_bat):
            score=score+h_bat
        if(r_bowl==h_bat or (score<scorer and s=='min') or (score>scorer and s=='max')):
            return score
            break

def h_bowl(scoreh,s):
    score=0
    while(True):
        r_bat=r.randint(0,6)
        try:
            h_bowl=int(input('\n\t\t* Enter your NUM SCORE [ 0 TO 6 ] for BOWL : '))
        except:
            print('\n\t\t ERROR ! INT TYPE only !')
        print('\n\t\t* MY NUM SCORE [ 0 TO 6 ] for BAT : ',r_bat)
        if(r_bat!=h_bowl):
            score=score+r_bat
        if(r_bat==h_bowl or (score>scoreh and s=='max') or (score<scoreh and s=='min')):
            return score
            break


a=input("\n\t\t Enter YES to START GAME or NO to QUIT :")
print("\n\t\t >>> USE INT TYPE and BLOCK LETTERS ONLY !")
print("\n---------------------------------------------------------------------------------------")
while (a=='YES'):
    print("\n\t\t >>> ODD or EVEN GAME !")
    h_c=input('\n\t\t* Enter your choice [ EVEN or ODD ] : ')
    l=['EVEN','ODD','BAT','BOWL']
    r_eo=r.randint(0,1)
    print('\n\t\t* my choice is :',l[r_eo])
    if (h_c==l[r_eo]):
        print("\n\t\t >>> SAME CHOICE GIVEN !")
    else:
        h_cn=int(input('\n\t\t* Enter your NUM [ INT only ]: '))
        r_n=r.randint(0,6)
        check=h_cn+r_n
        print('\n\t\t* my choice is :',r_n)
        print('\n\t\t* TOTAL NUM :',check)
        scoreh,scorer=0,0
    
    
        if(check%2==0):
            if(h_c=='EVEN'):
                scoreh,scorer=h_1st()
                
            
            elif(l[r_eo]=='EVEN'):
                scoreh,scorer=r_1st()


        elif(check%2!=0):
            if(h_c=='ODD'):
                scoreh,scorer=h_1st()

            elif(l[r_eo]=='ODD'):
                scoreh,scorer=r_1st()

                    
        print("\n---------------------------------------------------------------------------------------")            
        if(scorer>scoreh):
            print('\n\t\t >>> I WON THE GAME !\n')
        elif(scorer==scoreh):
            print('\n\t\t >>> MATCH TIED !\n')
        else:
            print('\n\t\t >>> YOU WON THE GAME !\n')
    print("\n---------------------------------------------------------------------------------------")    
    a=input("\n\t Enter YES to START NEW GAME or NO to QUIT :")
    
    
