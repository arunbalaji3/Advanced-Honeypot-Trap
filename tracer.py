import webbrowser
import socket as sock

url = "https://localhost/index.html"
b = webbrowser.open_new_tab(url)

def tracer():
    webbrowser.open_new_tab(url)

def tracer2():
    try:
        get_socket_con = sock(sock.AF_INET,sock.SOCK_STREAM)
        get_socket_con.listen(10)
        while 1:
            client_con = get_socket_con.accept()
            client_con.send(b)
    except sock.error as identifier:
        print("[+] Unspecified error [{}]".format(identifier))
    except KeyboardInterrupt as ky:
        print("[-] Process stopped !")
    finally:
        get_socket_con.close()
    get_socket_con.close()

def tracer3(ip_add):
    try:
        ip_address = ip_add
        print(ip_address)
        url = 'http://localhost/index.html'

        get_socket_con = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        get_socket_con.bind((ip_address,443))
        get_socket_con.listen(10)

        while 1:
            client_con = get_socket_con.accept()

            client_con.send(url.encode())

            client_con.send(url)
            
            client_con.close()

    except sock.error as identifier:
        print(f"[+] Unspecified error [{identifier}]")
    except KeyboardInterrupt:
        print("[-] Process stopped !")
    finally:
        get_socket_con.close()
    get_socket_con.close()

if __name__ == "__main__":
    tracer3()
