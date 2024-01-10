import requests
import json

def check_vpn2(ip_address):
    api_key = "aebe2bf1e35d6874b56cd7fe92ae1fade4725e7dfd3b0705311d5b7a"
    url = f"https://api.ipdata.co/{ip_address}/threat?api-key={api_key}"
    response = requests.get(url)
    result = response.json()
    if "is_proxy" in result and result["is_threat"]:
        return True
    else:
        return False
    
def check_vpn(ip_address):
    ip_add = ip_address
    api_key = "aebe2bf1e35d6874b56cd7fe92ae1fade4725e7dfd3b0705311d5b7a"
    url = f"https://api.ipdata.co/{ip_add}?api-key={api_key}"
    response = requests.get(url)
    result = json.dumps(response.json())
    with open("arun.txt","a") as f:
        f.write('\n\n'+result)
    if isinstance(result, str):
        result = json.loads(result)
    if "threat" in result:
        is_threat = result["threat"]["is_threat"]
        if is_threat:
            return True
        else:
            return False
    else:
        print("An error occurred while checking for threat.")

if __name__ == "__main__":
    client_ip = input("Enter client IP address: ")
    if check_vpn2(client_ip):
        print("Request blocked: VPN usage detected")
    else:
        print("Request allowed")


