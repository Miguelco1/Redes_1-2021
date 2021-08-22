import socket
import sys 
import os
import re
from datetime import datetime
import selectors
import types
import time
def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    sock_list.append(conn)
    now = datetime.now() # current date and time
    date_time = now.strftime("%H:%M:%S")
    print(date_time,'>>Connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ 
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    global count_connect
    sock = key.fileobj
    data_add=key.data
    name_pass=0
    if mask & selectors.EVENT_READ:
        try:
            data = sock.recv(2048)  # Should be ready to read
            print("Data received:",data)
            opcode=data[0]
        except:
            data=-1
        if data:
            #Transforma a mensagem de binario para string
            try:
                end_byte=bytearray([0])
                opcode=data[0]
                if opcode==1:
                    decode_name=data[1:].decode("utf-8", "ignore")
                    if next((item for item in name_list if item["name"] == decode_name.strip()), False):
                        print("Nome Indisponivel")
                        opcode_ack=[1,1] 
                        array=bytearray(opcode_ack)
                        sock.sendall(array+end_byte)

                        pass
                    else:
                        if count_connect==0:
                            count_connect=1
                        else:
                            count_connect = count_connect << 1


                        count_aux=bytearray([count_connect])
                        name={"name":decode_name,"addr":data_add.addr,"sock":sock,"count":count_aux}
                        name_list.append(name)
                        
                        opcode_ack=bytearray([1,2]) 
                        sock.sendall(opcode_ack+end_byte)
                        opcode_ack=bytearray([3]) 
                        send_init_online=opcode_ack
                        sep_aux=bytearray(" ",'utf-8')

                        for item in name_list:
                            aux=bytearray(item.get("count"))
                            name_aux=bytearray(item.get("name"),'utf-8')
                            send_init_online=send_init_online+sep_aux+aux+sep_aux+name_aux
                        sock.sendall(send_init_online+end_byte)

                        opcode_ack=bytearray([4]) 
                        send_new_user_online=opcode_ack
                        name_aux2=bytearray(decode_name,'utf-8')
                        send_new_user_online=send_new_user_online+sep_aux+count_aux+sep_aux+name_aux2
                                        
                        for conn in sock_list:
                            if conn==sock:
                                continue
                            conn.sendall(send_new_user_online+end_byte)


                        opcode_ack=bytearray([2])
                        connect_msg=name.get("name")+" ---> Entrou no chat!"
                        connect_msg=opcode_ack+bytearray(connect_msg,"utf-8")

                        for conn in sock_list:
                            conn.sendall(connect_msg+end_byte)



                elif opcode==2:
                    dests=data[1]
                    msg_receiv=data[2:]
                    sender= next((item for item in name_list if item["sock"] == sock))
                    sender=sender.get("name")
                    sender=sender+": "
                    sender=bytearray(sender,"utf-8")
                    opcode_ack=bytearray([2])
                    msg_send=opcode_ack+sender+msg_receiv
                    for conn in name_list:
                        count_aux=int.from_bytes(conn.get("count"),"big")
                        if (count_aux & dests):
                            conn_send=conn.get("sock")
                            conn_send.sendall(msg_send+end_byte)


            except:
                if (data!=-1):
                    print("Mensagem com Formato invalido recebida from",data_add.addr)
                now = datetime.now() # current date and time
                date_time = now.strftime("%H:%M:%S")
                try:
                    del_sock= next((item for item in name_list if item["addr"] == data_add.addr), False)
                    name_del=del_sock.get("name")
                    name_list.remove(del_sock)
                    name_pass=1
                except:
                    pass
                print(date_time,">>Connection from",data_add.addr,"closed")
                if (data!=-1):
                    opcode_ack=bytearray([5]) 
                    send_end_online=opcode_ack
                    sock.sendall(send_end_online)
                sel.unregister(sock)
                sock.close()
                sock_list.remove(sock)
                if (name_pass==1):
                    count_connect = count_connect >> 1
                    new_count=1
                    for update_del_name_list in name_list:
                        aux_count=bytearray([new_count])
                        update_del_name_list["count"]=aux_count
                        new_count=new_count << 1

                    opcode_ack=bytearray([3]) 
                    send_init_online=opcode_ack
                    sep_aux=bytearray(" ",'utf-8')

                    for item in name_list:
                        aux=bytearray(item.get("count"))
                        name_aux=bytearray(item.get("name"),'utf-8')
                        send_init_online=send_init_online+sep_aux+aux+sep_aux+name_aux
                    for conn in sock_list:
                        conn.sendall(send_init_online+end_byte)


                    opcode_ack=bytearray([2])

                    disconnect_msg=name_del+" ---> Saiu do chat!"
                    disconnect_msg=opcode_ack+bytearray(disconnect_msg,"utf-8") 
                    for conn in sock_list:
                        conn.sendall(disconnect_msg+end_byte)

                return()


            #Verifica se o id da conexão já está no webserver,
            #Se não estiver coloca ele lá


        else:
            #Nunca é para receber uma string vazia, já que qualquer envio possui opcode
            now = datetime.now() # current date and time
            date_time = now.strftime("%H:%M:%S")
            try:
                del_sock= next((item for item in name_list if item["addr"] == data_add.addr), False)
                name_list.remove(del_sock)
            except:
                pass
            print(date_time,">>Connection from",data_add.addr,"closed")
            sel.unregister(sock)
            sock.close()
            sock_list.remove(sock)

name_list=[]
sock_list=[]
count_connect=0
sel = selectors.DefaultSelector()
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('25.94.104.82', 5015)
print('starting up on {} port {}'.format(*server_address))
s.bind(server_address)

# Listen for incoming connections
s.listen(8)
s.setblocking(False)
sel.register(s, selectors.EVENT_READ, data=None)
print('Accepting connections')
while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key, mask)

