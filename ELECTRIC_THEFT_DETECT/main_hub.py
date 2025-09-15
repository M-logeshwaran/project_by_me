import random
import socket
import time
  
class main_hub:
    def __init__(self):
        pass

sub_hub = {}  # client socket dict

server_hub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_hub.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_hub.bind(("0.0.0.0", 6000))
server_hub.listen(2)
print("Server listening on port 6000...")

k = 1
while k <= 2:
    client_socket1, addr = server_hub.accept()
    sub_hub[k] = client_socket1
    print(addr, " is connected !")
    k += 1

try:
    if int(sub_hub[1].recv(1024).decode()) == 1:
        pass
    if int(sub_hub[2].recv(1024).decode()) == 2:
        pass
    else:
        temp = sub_hub[1]
        sub_hub[1] = sub_hub[2]
        sub_hub[2] = temp
except Exception as e:
    print("[MainHub] Error during ID exchange:", e)

k = 1
while True:
    try:
        time.sleep(2)
        print("\n", "-" * 100, "\n")
        print("\n\t", k, " FLOW :")

        input_volt = str(random.randint(240, 245))
        print("\n\t\tinput voltage : ", input_volt)

        sub_hub[1].send(input_volt.encode())
        sub_recive_volt = int(sub_hub[1].recv(1024).decode())
        print("\n\t\tSUB 1 recive voltage : ", sub_recive_volt)

        if(sub_recive_volt == 0):
            print("\n\n\tWIRE WAS CUTTED ! \n")
            addr_sub = sub_hub[1].recv(1024).decode()
            print("From sub_hub Between :", addr_sub)
            print("\n\n\tCUTTENT FLOW WAS STOPPED ! in BEFORE SUB_HUB OF subhub ", addr_sub)

            # send voltage=0 and subid together
            sub_hub[2].send(f"0,{addr_sub}\n".encode())

        elif sub_recive_volt < 235:
            print("\n\n\tTHEFT DETECTED ! \n")
            theft_data = sub_hub[1].recv(3000).decode()

            if theft_data:
                input_server_volt, recivied_sub_voolt, diff_volt, addr_sub = theft_data.split(",")
                print("From SubHub:", addr_sub)

                # send theft data with prefix
                sub_hub[2].send(f"T,{theft_data}\n".encode())

        k += 1

    except Exception as e:
        print("\n[MainHub] Error in loop:\n", e)
        break    
