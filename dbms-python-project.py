import csv
import mysql.connector as m

def showdatabases():
    try:
       c.execute("show DATABASES;")
       data=c.fetchall()
       print("\n\t    >>> DATABASES in PC :")
       for i in data:
            print("\n\t\
      *",*list(i),sep=" ")
    except:
        print("\n\t\tNO DATABASES ARE CREATED !")

            
def showtables():
    try:
       c.execute("show tables;")
       data=c.fetchall()
       print("\n\t    >>> TABLES in DB :")
       for i in data:
            print("\n\t\
      *",*list(i),sep=" ")
    except:
        print("\n\t\tNO TABLES ARE CREATED !")

            
def usedata(s):
    try:
       c.execute("use "+s+";")
       print("\n\
       connected with "+s+" named database")
    except:
        print("\n\t\tERROR ! NO DATABASE FOUND !")

        
def desc(s):
    c.execute("desc "+s+";")
    data2=c.fetchall()
    print("\n\t    >>> DESC TABLE "+s+" :")
    print("\n\n\
         \t>>> FEILDS\tTYPE\tNULL\tKEY\tDEFAULT\tEXTRA ")
    for i in data2:
        print("\n\t\
      *",*list(i),sep="\t")

        
def display(s):
    print("--------------------------------------------------------------------")
    c.execute("show columns from "+s+";")
    data4=c.fetchall()
    for i in data4:
            print(i[0],"\t",end="")  
    print("\n--------------------------------------------------------------------")
    c.execute("select * from "+s+";")
    data3=c.fetchall()
    for i in data3:
        #print("* ",end="")
        for j in i:
            print("* ",end="")
            print((j),
                  "\t\t",end="")   
        print("\n")
    print("--------------------------------------------------------------------")



print("\n\t\t\
      >>> LOGIN PAGE :")
user_name=input("\n\t\t* enter USER NAME : ")
password=input("\n\t\t* enter PASSWORD : ")
s=input("\n\
       >>> enter YES to connect with DBMS or NO to quit : ")
connection=False



if(s=="YES"):
    try:
       l=m.connect(host="localhost",user=user_name,passwd=password,database="loki")
       if l.is_connected():
             print("\n\t\t\tconnected sucessfully !")
             connection=True
       c=l.cursor()
    except:
        print("\n\t\tERROR ! USER NAME or PASS is WRONG ! ")
    if(connection==True):
        while(True):
            print("\n--------------------------------------------------------------------")
            
            print("\n\t\t>>> DBMS OPERATION menu :\n")
            print("\
      0. enter 0 to USE DATABASE or CREATE DATABASE : \n\
      1. enter 1 to SHOW CURRENT DATABASE NAME :\n\
      2. enter 2 to SHOW TABLES in current database : \n\
      3. enter 3 to CREATE TABLES : \n\
      4. enter 4 to DESCRIBE TABLES : \n\
      5. enter 5 to INSERT into TABLE : \n\
      6. enter 6 to UPDATE into TABLE : \n\
      7. enter 7 to ALTER TABLE : \n\
      8. enter 8 to DISPLAY INFORMATION IN TABLE : \n\
      9. enter 9 to SAVE TABLE IN CSV FILE : \n\
     10. enter 10 to DELETE ROWS from TABLE : \n\
     11. enter 11 to DROP TABLE or DROP DATABASE : \n\
     12. enter 12 to QUIT : \n")
            

            
            op=input("\n\
      * enter your choice from above menu: ")


            if(op=='0'):
                    while(True):
                           print("\n--------------------------------------------------------------------")
                           print("\n\t\t>>> DATABASES menu :\n")
                           print("\
      1. enter 1 to USE DATABASE : \n\
      2. enter 2 to CREATE DATABASE (AUTO USE) :\n\
      3. enter 3 to SHOW DATABASES AVAILABLE in PC : \n\
      4. enter 4 to QUIT DATABASE MENU :\n")
                           dp=input("\n\
      * enter your choice from above menu: ")

                           
                           if(dp=='1'):
                                  print("\n\
      >>> USE DATABASE :")
                                  d_name=input("\n\
      * enter your DATABASE NAME to USE : ")
                                  usedata(d_name)


                           elif(dp=='2'):
                               print("\n\
      >>> CREATE NEW DATABASE :")
                               dn_name=input("\n\
      * enter your NEW DATABASE NAME to CREATE : ")
                               try:
                                  c.execute("create database "+dn_name+";");
                                  print("\n\
      >>> NEW DATABASE CREATED :\n")
                                  usedata(dn_name)
                               except:
                                   print("\n\t\tERROR ! INPUT FORMAT is WRONG !\n\
     #or DATABASE ALREADY EXIST !")



                           elif(dp=='3'):
                                showdatabases()



                           elif(dp=='4'):
                                print("\n\t\tDATABASES MENU as been CLOSED !")
                                break


                           else:
                               print("\n\t\tERROR ! INVALID CHOICE GIVIEN !\n")
                                 
            


            if(op=='1'):
                print("\n\
      connected with loki named database")
                


            elif(op=='2'):
                showtables()

                    


            elif(op=='3'):
                print("\n\
      >>> CREATE TABLES :")
                cn=int(input("\n\
      * enter the num of column :"))
                column=""
                t_name=input("\n\
      * enter TABLE NAME :")
                
                for i in range(cn):
                    datac=input("\n\
      * enter the [ COLUMN NAME - DATATYPE - CONSTRAINT(opt) ] :")
                    if(i!=(cn-1)):
                        column=column+datac+","
                    else:
                        column=column+datac
                try:        
                    c.execute("create table "+t_name+"("+column+")"+";")
                    print("\n\
     CREATED SUCCESSFULLY !")
                except:
                    print("\n\t\tERROR ! INPUT FORMAT is WRONG !\n\
     or REPEATED COLUMN GIVIEN !\n\
     or TABLE ALREADY EXIST !")

                    


            elif(op=='4'):
                t_name2=input("\n\
      * enter the TABLE NAME :")
                try:
                   desc(t_name2)
                except:
                   print("\n\t\tERROR ! NO TABLE FOUND !")

                    


            elif(op=='5'):
                 print("\n\
      >>> INSERT INTO TABLES :")
                 rn=int(input("\n\
      * enter the num of ROWS :"))
                 rows=""
                 r_name=input("\n\
      * enter TABLE NAME :")
                 try:
                    display(r_name)
                    for i in range(rn):
                        datar=input("\n\
      * enter the VALUES for corresponding COLUMN [ values,values..] :")
                        c.execute("insert into "+r_name+" values("+datar+");")
                    l.commit()
                    display(r_name)
                    print("\n\
      INSERTED SUCCESSFULLY !\n")
                 except:
                     print("\n\t\tERROR ! NO TABLE FOUND !\n\
               or INPUT FORMAT is WRONG !")

                     


            elif(op=='6'):
                print("\n\
      >>> UPDATE INTO TABLES :")
                u_name=input("\n\
      * enter TABLE NAME :")
                try:
                   display(u_name)
                   u_values=input("\n\
      * enter the VALUES to be UPDATE with CORRESPONDING COLUMN [ COLUMN=VALUE ] :")
                   u_condition=input("\n\
      * enter the CONDITION WHERE to be UPDATE [ COLUMN=CONDITION ]:")
                   c.execute("update "+u_name+" set "+u_values+" where "+u_condition+";")
                   print("\n\
      UPDATED SUCCESSFULLY !\n")
                   l.commit()
                   display(u_name)
                except:
                    print("\n\t\tERROR ! NO TABLE FOUND !\n\
               or INPUT FORMAT is WRONG !")

                    


            elif(op=='8'):
                try:
                   s_name=input("\n\
      * enter TABLE NAME :")
                   print("\n\
      >>> TABLE",s_name,";")
                   display(s_name)
                except:
                    print("\n\t\tERROR ! NO TABLE FOUND !")

                    


            elif(op=='7'):
                while(True):
                    print("\n--------------------------------------------------------------------")
                    print("\n\t\t>>> ALTER menu :")
                    print("\n\
      1. enter 1 to ADD COLUMN :\n\
      2. enter 2 to MODIFY DATABASE(SIZE) and CHANGE COLUMN POSITION(opt) : \n\
      3. enter 3 to CHANGE COLUMN NAME-DATATYPE : \n\
      4. enter 4 to DELETE KEYS or COLUMN : \n\
      5. enter 5 to QUIT ALTER MENU : \n")
                    ap=input("\n\
      enter your choice from above menu: ")
                    if(int(ap)<5):
                        al_name=input("\n\
      * enter TABLE NAME :")
                        


                    
                    if(ap=='1'):
                        try:
                           display(al_name)
                           print("\n\
      >>> ADD COLUMN INTO TABLE :")
                           ac_name=input("\n\
      * enter [ NEW COLUMN NAME - DATATYPE - KEY(opt) ] to ADD :")
                           c.execute("alter table "+al_name+" add "+ac_name+";")
                           print("\n\
      COLUMN ADDED SUCCESSFULLY !\n")
                           l.commit()
                           display(al_name)
                        except:
                            print("\n\t\tERROR ! NO TABLE FOUND !\n\
               or INPUT FORMAT is WRONG !")
                            
                            

                        
                    elif(ap=='2'):
                        try:
                           desc(al_name)
                           print("\n\
      >>> MODIFY INTO TABLE :")
                           m_column=input("\n\
      * enter [ COLUMN NAME - NEW DATATYPE - KEY(opt) - AFTER COLUMN NAME ]  :")
                           c.execute("alter table "+al_name+" modify "+m_column+";")
                           print("\n\
      MODIFIED SUCCESSFULLY !\n")
                           l.commit()
                           desc(al_name)
                        except:
                            print("\n\t\tERROR ! NO TABLE FOUND !\n\
               or INPUT FORMAT is WRONG !")

                            


                    elif(ap=='3'):
                        try:
                           display(al_name)
                           print("\n\
      >>> CHANGE COLUMN NAME :")
                           c_column=input("\n\
      * enter [ OLD COLUMN NAME - NEW COLUMN - DATATYPE - KEY(opt) ]  :")
                           c.execute("alter table "+al_name+" change "+c_column+";")
                           print("\n\
      COLUMN NAME CHANGED SUCCESSFULLY !\n")
                           l.commit()
                           display(al_name)
                        except:
                           print("\n\t\tERROR ! NO TABLE FOUND !\n\
               or INPUT FORMAT is WRONG !")
                           
                         


                    elif(ap=='4'):
                        try:
                           display(al_name)
                           print("\n\
      >>> DELETE KEY AND COLUMN :")
                           d_column=input("\n\
      * enter COLUMN-NAME or KEY NAME or BOTH to DELETE :")
                           c.execute("alter table "+al_name+" drop "+d_column+";")
                           print("\n\
      DELETED SUCCESSFULLY !\n")
                           l.commit()
                           display(al_name)
                        except:
                            print("\n\t\tERROR ! NO TABLE FOUND !\n\
               or INPUT FORMAT is WRONG !")



                    elif(ap=='5'):
                          print("\n\t\tALTER MENU has been CLOSED !")
                          break

                        
                    else:
                        print("\n\t\tERROR ! INVALID CHOICE GIVIEN !")
                    


                    
            elif(op=='9'):
                print("\n\
      >>> TABLE SAVE IN CSV FILE :")
                f_name=input("\n\
      * enter FILE NAME :")
                ft_name=input("\n\
      * enter TABLE NAME :")
                try:
                   fp=open(f_name+".csv","w")
                   w=csv.writer(fp)
                   c.execute("show columns from "+ft_name+";")
                   data5=c.fetchall()
                   rowses=[]
                   for i in data5:
                         rowses.append(i[0])
                   w.writerow(rowses)      
                   c.execute("select * from "+ft_name+";")
                   data6=c.fetchall()
                   w.writerows(data6)
                   fp.close()
                   print("\n\
      TABLE RECORDS as been SAVED SUCCESSFULLY !\n")
                except:
                    print("\n\t\tERROR ! NO TABLE FOUND !")




            elif(op=='10'):
                try:
                    d_t=input("\n\
      * enter TABLE NAME :")
                    display(d_t)
                    print("\n\
      >>> DELETE ROWS FROM TABLE :")
                    d_r=int(input("\n\
      * enter NUM of ROWS to DELETE :"))
                    for i in range(d_r):
                         d_c=input("\n\
      * enter CONDITION [ COLUMN=VALUES ]:")
                         c.execute("delete from "+d_t+" where "+d_c+";" )
                    l.commit()
                    display(d_t)
                    print("\n\
      ROWS ARE DELETED SUCCESSFULLY !\n")
                except:
                     print("\n\t\tERROR ! NO TABLE FOUND !\n\
               or INPUT FORMAT is WRONG !\n\
               or ROWS NOT FOUND IN TABLE !")

                
                    
            elif(op=='11'):
                while(True):
                    print("\n--------------------------------------------------------------------")
                    print("\n\t\t>>> DROP menu :")
                    print("\n\
      1. enter 1 to DELETE TABLE :\n\
      2. enter 2 to DELETE DATABASES :\n\
      3. enter 3 to QUIT : \n")
                    de=input("\n\
      enter your choice from above menu: ")

                    
                    if(de=='1'):
                        try:
                           showtables()
                           de_tname=input("\n\
      * enter TABLE NAME :")
                           c.execute("drop table "+de_tname+";")
                           print("\n\
      TABLE "+de_tname+" DELETED SUCCESSFULLY !\n")
                        except:
                             print("\n\t\tERROR ! NO TABLE FOUND !")


                    elif(de=='2'):
                        try:
                            showdatabases()
                            de_dname=input("\n\
      * enter TABLE NAME :")
                            c.execute("drop database "+de_dname+";")
                            print("\n\
      DATABASE "+de_dname+" DELETED SUCCESSFULLY !\n")
                        except:
                             print("\n\t\tERROR ! NO TABLE FOUND !")


                    elif(de=='3'):
                         print("\n\t\tDROP MENU as been CLOSED !")
                         break


                    else:
                        print("\n\t\tERROR ! INVALID CHOICE GIVIEN !")



                    
            elif(op=='12'):
                l.close()
                print("\n\t\tDBMS has been CLOSED !")
                break


            else:
                print("\n\t\tERROR ! INVALID CHOICE GIVIEN !")
    
    
      
