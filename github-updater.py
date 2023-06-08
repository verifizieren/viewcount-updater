import requests
from time import sleep

welcome_art = """
 _____ _ _   _           _       _   _ _                        
|  __ (_| | | |         | |     | | | (_)                       
| |  \/_| |_| |__  _   _| |__   | | | |_  _____      _____ _ __ 
| | __| | __| '_ \| | | | '_ \  | | | | |/ _ \ \ /\ / / _ | '__|
| |_\ | | |_| | | | |_| | |_) | \ \_/ | |  __/\ V  V |  __| |   
 \____|_|\__|_| |_|\__,_|_.__/   \___/|_|\___| \_/\_/ \___|_|                                                            
"""

def requester(url):
    re = requests
    req = re.get(url=url) # Requesting given URL
    return req.status_code

class github_update:
    print(welcome_art + "\n") # Prints the welcome art
    target = input(f"[*] Please input your viewcount link: ") # Getting the target URL
    req_amount = int(input(f"[*] Please input number of requets: ")) # Getting Request amount

    for i in range(req_amount):
        req = requester(target)
        if req == 200:  # Checking status code
            print("Succesfull")
        else:
            print("Failed")
        #sleep(1)

def main():
    github_update()

if __name__ == "__main__":
    main()