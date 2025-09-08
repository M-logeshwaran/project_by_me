import random
import socket
import time

sub_hub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ip_address = input("\n\nEnter the IP ADDRESS of SERVER ! :")
    sub_hub.connect((ip_address, 6000))
    sub_id = "1"
    sub_hub.send(sub_id.encode())
except Exception as e:
    print("\n[SubHub] Connection error:\n", e)
    exit()

while True:
    try:
        time.sleep(2)
        print("\n", "-" * 100, "\n")
        print("\n\t\tSUB_HUB_1 REPORT : ")

        get_volt = sub_hub.recv(1024).decode()
        if not get_volt:
            print("\n[SubHub] Server closed connection\n")
            break

        get_volt = int(get_volt)
        print("\n\tINCOMING voltage : ", get_volt)

        rt = random.randint(1, 5)
        re = random.randint(1, 5)
        if rt == 1 and re==1 :
            theft = 0
            get_volt = 0
        elif rt==1 :
            theft = random.randint(15,30)
        else:
            theft = random.randint(0, 3)

        input_volt = get_volt - theft
        sub_hub.send(str(input_volt).encode())
        print("\n\tRECIVED voltage : ", input_volt)


        if(input_volt == 0 ):
            print("\n\t WIRE CUT WAS DETECTED ! ")
            
        elif input_volt < 235:
            print("\n\tTHEFT DETECTED ! ")
            theft_data = f"{get_volt},{input_volt},{theft},{sub_id}"
            sub_hub.send(theft_data.encode())

    except Exception as e:
        print("\n[SubHub] Error in loop:\n", e)
        break
