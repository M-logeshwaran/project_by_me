import socket
import time
import pandas as pd
from datetime import datetime
import pygame
import mysql.connector as msql
 
app_hub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ip_address = input("\n\nEnter the IP ADDRESS of SERVER ! :")
    app_hub.connect((ip_address, 6000))
    app_id = "2"
    app_hub.send(app_id.encode())
except Exception as e:
    print("[App] Connection error:", e)
    exit()

ms = msql.connect(host="localhost",user="root",passwd="root123",database="loki")
mc = ms.cursor()
mc.execute("create table THEFT(INCOMING_VOLT varchar(20),RECIEVED_VOLT varchar(20),THEFTED_VOLT varchar(20),ADDRESS_OF_SUB_HUB varchar(20),DATE varchar(20), TIME varchar(20))")
mc.execute("create table WIRE(REPORT_FROM_SUB_HUB varchar(20),STATUS varchar(20),DATE varchar(20), TIME varchar(20))")
pygame.mixer.init()
theft_sound = pygame.mixer.Sound(r"C:\Users\Admin\OneDrive\Pictures\THEFT_SOUND.mp3")
cut_sound = pygame.mixer.Sound(r"C:\Users\Admin\OneDrive\Pictures\Wire.mp3")

l1, l2, l3, l4, l5, l6 = [], [], [], [], [], []

while True:
    try:
        time.sleep(2)
        data = app_hub.recv(2000).decode().strip()
        if not data:
           print("[App] Connection closed by server")
           break

        # split in case multiple messages arrived
        for msg in data.split("\n"):
            if not msg:
                continue

            # cut case: "0,1"
            if "," in msg and not msg.startswith("T"):
                parts = msg.split(",")
                if len(parts) == 2 and parts[0] == "0":
                    addr_sub = parts[1]

                    cut_sound.play()
                    while pygame.mixer.music.get_busy():
                        continue
                    now_date = datetime.now().strftime("%Y-%m-%d")
                    now_time = datetime.now().strftime("%H:%M:%S")
                    mc.execute("insert into WIRE values('{}','{}','{}','{}');".format(addr_sub,"WIRE CUTED",now_date ,now_time))
                    ms.commit()
                    print("\n", "-" * 100, "\n")
                    print("\n\n\tWIRE WAS CUTTED ! \n")
                    print("From sub_hub Between :", addr_sub)
                    print("\n\n\tCUTTENT FLOW WAS STOPPED !\n\nBEFORE SUB_HUB : ", addr_sub)

            # theft case: "T,245,225,20,1"
            elif msg.startswith("T,"):

                theft_sound.play()
                while pygame.mixer.music.get_busy():
                    continue

                theft_data = msg[2:]  # remove "T,"
                incoming_volt, recivied_volt, diff_volt, addr_sub = theft_data.split(",")

                now_date = datetime.now().strftime("%Y-%m-%d")
                now_time = datetime.now().strftime("%H:%M:%S")
                l1.append(incoming_volt)
                l2.append(recivied_volt)
                l3.append(diff_volt)
                l4.append(addr_sub)
                l5.append(now_date)
                l6.append(now_time)

                df = {
                '   INCOMING_VOLT   ': l1,
                '   RECIEVED_VOLT   ': l2,
                '   THEFTED_VOLT   ': l3,
                '   ADDRESS_OF_SUB_HUB   ': l4,
                '   DATE   ': l5,
                '   TIME   ': l6
                 }
                mc.execute("insert into THEFT values('{}','{}','{}','{}','{}','{}');".format(incoming_volt, recivied_volt, diff_volt, addr_sub ,now_date ,now_time))
                ms.commit()
                print("\n", "-" * 100, "\n")                                                                          
                print("\n\t\tALERT ! THEFT DETECTED !\n")
                data_fr = pd.DataFrame(df)
                print(data_fr)
                
    except Exception as e:
        print("\n[AppHub] Error in loop:\n", e)
        break            

ms.close()
app_hub.close()
