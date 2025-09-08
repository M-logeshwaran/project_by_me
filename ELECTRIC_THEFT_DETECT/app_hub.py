import socket
import time
import pandas as pd
from datetime import datetime

app_hub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ip_address = input("\n\nEnter the IP ADDRESS of SERVER ! :")
    app_hub.connect((ip_address, 6000))
    app_id = "2"
    app_hub.send(app_id.encode())
except Exception as e:
    print("[App] Connection error:", e)
    exit()

l1, l2, l3, l4, l5, l6 = [], [], [], [], [], []

while True:
    try:
        time.sleep(2)
        print("\n","-"*100,"\n")
        data = app_hub.recv(1024).decode()

        if not data:
            print("[App] Connection closed by server")
            break
        
        now_date=datetime.now().strftime("%Y-%m-%d")
        now_time=datetime.now().strftime("%H:%M:%S")
        incoming_volt, recivied_volt, diff_volt, addr_sub = data.split(",")
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

        print("\n\t\tALERT ! THEFT DETECTED !\n")
        data_fr = pd.DataFrame(df)
        print(data_fr)

    except Exception as e:
        print("[App] Error receiving data:", e)
        break
