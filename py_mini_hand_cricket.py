import random as r

def h_1st():
    scoreh,scorer=0,0
    print("\n---------------------------------------------------------------------------------------")
    print('\n\t\t >>> YOU WON THE TOSS :')
    h_ebc=input('\n\t\t* Enter your choice [ BAT OR BOWL ] : ')
    if(h_ebc=='BAT'):
        scoreh=h_bat(scorer,'min')
        print("\n---------------------------------------------------------------------------------------")
        print('\n\t\t >>> YOUR TOTAL SCORE :',scoreh)
        print('\n\t\t >>> COMP TARGET :',scoreh+1)
        print("\n---------------------------------------------------------------------------------------")
        print("\n\t\t SIDE CHANGE !")
        print("\n---------------------------------------------------------------------------------------")
        scorer=h_bowl(scoreh,'max')
        print("\n---------------------------------------------------------------------------------------")
        print('\n\t\t >>> COMP TOTAL SCORE :',scorer)
        print('\n\t\t >>> YOUR TOTAL SCORE :',scoreh)
        return scoreh,scorer
    elif(h_ebc=='BOWL'):
        scorer=h_bowl(scoreh,'min')
        print("\n---------------------------------------------------------------------------------------")
        print('\n\t\t >>> COMP TOTAL SCORE :',scorer)
        print('\n\t\t >>> YOUR TARGET :',scorer+1)
        print("\n---------------------------------------------------------------------------------------")
        print("\n\t\t SIDE CHANGE !")
        print("\n---------------------------------------------------------------------------------------")
        scoreh=h_bat(scorer,'max')
        print("\n---------------------------------------------------------------------------------------")
        print('\n\t\t >>> YOUR TOTAL SCORE :',scoreh)
        print('\n\t\t >>> COMP TOTAL SCORE :',scorer)
        return scoreh,scorer

def r_1st():
    scoreh,scorer=0,0
    r_bb=r.randint(2,3)
    print("\n---------------------------------------------------------------------------------------")
    print('\n\t\t >>> I WON THE TOSS :')
    print('\n\t\t* MY choice [ BAT OR BOWL ] : ',l[r_bb])
    if(l[r_bb]=='BOWL'):
        scoreh=h_bat(scorer,'min')
        print("\n---------------------------------------------------------------------------------------")
        print('\n\t\t >>> YOUR TOTAL SCORE :',scoreh)
        print('\n\t\t >>> COMP TARGET :',scoreh+1)
        print("\n---------------------------------------------------------------------------------------")
        print("\n\t\t SIDE CHANGE !")
        print("\n---------------------------------------------------------------------------------------")
        scorer=h_bowl(scoreh,'max')
        print("\n---------------------------------------------------------------------------------------")
        print('\n\t\t >>> COMP TOTAL SCORE :',scorer)
        print('\n\t\t >>> YOUR TOTAL SCORE :',scoreh)
        return scoreh,scorer
    elif(l[r_bb]=='BAT'):
        scorer=h_bowl(scoreh,'min')
        print("\n---------------------------------------------------------------------------------------")
        print('\n\t\t >>> COMP TOTAL SCORE :',scorer)
        print('\n\t\t >>> YOUR TARGET :',scorer+1)
        print("\n---------------------------------------------------------------------------------------")
        print("\n\t\t SIDE CHANGE !")
        print("\n---------------------------------------------------------------------------------------")
        scoreh=h_bat(scorer,'max')
        print("\n---------------------------------------------------------------------------------------")
        print('\n\t\t >>> YOUR TOTAL SCORE :',scoreh)
        print('\n\t\t >>> COMP TOTAL SCORE :',scorer)
        return scoreh,scorer

                    
def h_bat(scorer,s):
    score=0
    balls=0
    while(True):
        r_bowl=r.randint(0,6)
        try:
            h_bat=int(input('\n\t\t* Enter your NUM SCORE [ 0 TO 6 ] for BAT : '))
        except:
            print('\n\t\t ERROR ! INT TYPE only !')
            continue
        print('\n\t\t* COMP NUM SCORE [ 0 TO 6 ] for BOWL : ',r_bowl)
        if(r_bowl!=h_bat):
            score=score+h_bat
            balls=balls+1
            print("\n---------------------------------------------------------------------------------------")
            if(score==50 and score<100):
                print("\n\t\t YOU REACH HALF CENTURY !")
            elif(score==100):
                print("\n\t\t YOU REACH CENTURY !")
            print('\n\t\t >>> YOUR CURRENT SCORE :',score)
            print('\n\t\t >>> BALLS :',balls)
        if(r_bowl==h_bat or (score<scorer and s=='min') or (score>scorer and s=='max')):
            return score
            break

def h_bowl(scoreh,s):
    score=0
    balls=0
    while(True):
        r_bat=r.randint(0,6)
        try:
            h_bowl=int(input('\n\t\t* Enter your NUM SCORE [ 0 TO 6 ] for BOWL : '))
        except:
            print('\n\t\t ERROR ! INT TYPE only !')
            continue
        print('\n\t\t* COMP NUM SCORE [ 0 TO 6 ] for BAT : ',r_bat)
        if(r_bat!=h_bowl):
            score=score+r_bat
            balls=balls+1
            print("\n---------------------------------------------------------------------------------------")
            if(score==50 and score<100):
                print("\n\t\t COMP REACH HALF CENTURY !")
            elif(score==100):
                print("\n\t\t COMP REACH CENTURY !")
            print('\n\t\t >>> COMP CURRENT SCORE :',score)
            print('\n\t\t >>> BALLS :',balls)
        if(r_bat==h_bowl or (score>scoreh and s=='max') or (score<scoreh and s=='min')):
            return score
            break


a=input("\n\t\t Enter YES to START GAME or NO to QUIT :")
print("\n\t\t >>> USE INT TYPE and BLOCK LETTERS ONLY !")
print("\n---------------------------------------------------------------------------------------")
while(True):
    if(a=="YES"):
        print("\n\t\t >>> ODD or EVEN GAME !")
        h_c=input('\n\t\t* Enter your choice [ EVEN or ODD ] : ')
        l=['EVEN','ODD','BAT','BOWL']
        r_eo=r.randint(0,1)
        print('\n\t\t* COMP choice is :',l[r_eo])
        if (h_c==l[r_eo]):
            print("\n\t\t >>> SAME CHOICE GIVEN !")
            print("\n---------------------------------------------------------------------------------------")
            continue
        else:
            h_cn=int(input('\n\t\t* Enter your NUM [ INT only ]: '))
            r_n=r.randint(0,6)
            check=h_cn+r_n
            print('\n\t\t* COMP choice is :',r_n)
            if(check%2==0):
                print('\n\t\t* TOTAL NUM :',check,'(EVEN)')
            else:
                print('\n\t\t* TOTAL NUM :',check,'(ODD)')
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
                 print('\n\t\t >>> COMP WON THE GAME !\n')
            elif(scorer==scoreh):
                 print('\n\t\t >>> MATCH TIED !\n')
            else:
                 print('\n\t\t >>> YOU WON THE GAME !\n')
    print("\n---------------------------------------------------------------------------------------")    
    a=input("\n\t Enter YES to START NEW GAME or NO to QUIT :")
    if(a=='NO'):
        print("\n\t\t >>> ODD or EVEN GAME has been CLOSED !")
        break
    else:
        continue
    
    
