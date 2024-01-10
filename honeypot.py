from socket import *
import requests
from flask import Flask, request, render_template
from vpn2 import check_vpn
from tracer import tracer3, tracer
import re
from alert import send_alert
from alert import send_alert2
import datetime
import sys
from locator import locator

def main():
    ip_add = "192.168.127.5"
    port = 80

    print("[+] Starting Honeypot.......")

    try:
        get_socket_con = socket(AF_INET,SOCK_STREAM)
        get_socket_con.bind((ip_add,port))
        get_socket_con.listen(10)
        
        print("[+] Honeypot started.......")
        a = 1

        while a:
            
            now = datetime.datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")

            ip_address = requests.get('https://api64.ipify.org').text
            with open("logs.txt", "a") as f:
                f.write("\n["+date_time+"]\n")
            if ip_address is not None:
                x = check_vpn(ip_address)
                a=1
            else:
                a=0
                print(ip_address)
                client_con,client_addr = get_socket_con.accept()
                client_con.send(b"<h1> failure in checking vpn type! </h1>")
                print("failure in checking vpn type!")
            if x == False:
                client_con,client_addr = get_socket_con.accept()
                with open("logs.txt", "a") as f:
                    f.write("visiter found! - [{}]".format(client_addr[0]))

                
                with open(r'C:\xampp\htdocs\location.txt', 'r') as f:
                    lines = f.readlines()
                    last_line = lines[-1]
                    lat, lng = last_line.strip().split(",")

                
                
                #b = tracer3(ip_add)
                b = tracer()
                send_alert()
                if b is not None:
                    client_con.send(b)
                client_con.send(b"<h1> Error 404! Access Denied!!! </h1>")
                data = client_con.recv(2048)
                str_data = data.decode('utf-8')
                with open("logs.txt", "a") as f:
                    f.write('\n'+str_data)
                    f.write(ip_address+'\n'+lat+'\t'+lng+'\n')
                    locator()
                    f.write("**********************************")
            else:
                client_con,client_addr = get_socket_con.accept()
                with open("log.txt", "a") as f:
                    f.write("Visiter found!  - [{}]".format(client_addr[0]))
                client_con.send(b"<h1> error vpn found! come back again..... </h1>")
                data = client_con.recv(2048)
                str_data = data.decode('utf-8')
                with open("log.txt", "a") as f:
                    f.write(str_data)
                    f.write(ip_address)

    except error as identifier:
        print("[+] Unspecified error [{}]".format(identifier))
        send_alert2()
    except KeyboardInterrupt as ky:
        print("[-] Process stopped !")
        send_alert2()
    finally:
        get_socket_con.close()
    get_socket_con.close()

if __name__ == "__main__":
    main()
