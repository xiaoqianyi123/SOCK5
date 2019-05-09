import select
import socket
import threading

def JX(sock):

    print("heellloooo")
    process=0;
    IPAD=None;
    ifconnect=0;
    while True:
        print("正在运行")
        ready = select.select([sock], [], [], 5)
        if ready[0]:
            data = sock.recv(4096)
        else:
            print("no coming data")
        print("fuckk")
        
        if (data == b'\x05\x01\x00'and process==0):
            sock.send(b"\x05\x00")
            process=process+1

            continue
        if (JSSOCK51(data)and process==1):
            sock.send(b'\x05\x00\x00\x03\t127.0.0.1\xff\xff')
            IPAD=JXSOCK52(data)
            print(IPAD)
            process=process+1

            continue
        if(process==2):
            print("success to access")
        else:
            break;
        while True:
            print(13)
            if(ifconnect==0):
                please = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                please.connect(IPAD)
                please.setblocking(0)
                ifconnect=1;
            if(data):
                please.send(data)
            print("88888888888888888888888888888888")
            print(data)
            print("8888888888888888888888888888888888")
            handshake=0
            while True:
                print(789)
                ready = select.select([please], [], [], 5)
                if ready[0]:
                    DATA = please.recv(4096)
                else:
                    break
                if(DATA):
                    print("1111111111111111111111111111111111111111111111111111111111")
                    print(DATA)
                    handshake=handshake+1;
                    print("1111111111111111111111111111111111111111111111111111111111")
                    sock.send(DATA)
                    print(handshake) 
                else:
                    break
            break;


def JXSOCK52(data):
    a=data[4]
    b=data[5:5+a].decode()
    c= int.from_bytes(data[5+a:7+a], byteorder='big', signed=False)
    IPAD=(b,c)
    return IPAD;
def JSSOCK51(data):
    if(data[0:4]==b'\x05\x01\x00\x03' and len(data)==7+data[4]):
        return True;
    else:
        return False;


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind(('127.0.0.1', 65535))
s.listen(5)
a=0
time=0
while (a==0):
    print("welcome")
    sock, addr = s.accept()
    t2 = threading.Thread(target=JX, args=(sock,))
    t2.start()
    a=1
















