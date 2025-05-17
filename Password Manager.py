import json
import os
from cryptography.fernet import Fernet
from pathlib import Path


# empty list to store them all here
passwords = []  # The list looks like: passwords = [sec_key('google.com', 'abc123'), sec_key('github.com', 'xyz789')]

class sec_key:
    def __init__(self, website, sekret):
        self.website = website
        self.sekret = sekret

    def to_dict(self):
        return {"Name of Site": self.website, "Password": self.sekret}

def input_system():
    website = input("Enter Name of Site : ")
    sekret = input("Enter Password: ")
    return sec_key(website, sekret)

secret = "1234" # change it before you use

print("Do you have the Password to access the system?? ")
try:
    verification = str(input("Enter the Password to access the system : "))
except Exception as e:
    print("Try Again. An error occured:", e)

location_key = os.path.join(os.path.dirname(__file__), 'secret_test.key')

# db location
location = os.path.join(os.path.dirname(__file__), 'db.txt')

# # Load the saved key
with open(location_key, "rb") as key_file: # "rb" means read byte
    key = key_file.read()

fernet = Fernet(key)

if verification == secret:
    while True:
        try:
            print("-------------------------------------------------------")
            first = input("Enter 'Start' to Start storing Passwords \nor Enter 'exit' to exit the app. \nor Enter 'check' to revisit last saved Passwords \nor Enter 'delete' to delete a Password:- ")
            if first.lower() == 'start':
                try:
                    ask = int(input("How many Passwords do you want to input here? : "))
                    for _ in range(ask):
                        passwords.append(input_system())  # storing passwords in 'passwords' list
                    
                    pass_dict = [key.to_dict() for key in passwords]  # convert list of password to a dictionary of password   
                                      
                    json_output = json.dumps(pass_dict, indent=4)     
                    encrypted = fernet.encrypt(json_output.encode())

                    
                    file = Path(location)
                    
                    if file.exists():
                        with open(location, 'rb') as f:
                            to_be_decrypted = f.read()
                        
                        sent_to_decrypt = fernet.decrypt(to_be_decrypted).decode() # decrypting the code
                        useable_data = json.loads(sent_to_decrypt)                  # turning them into json
                        useable_data.extend(pass_dict)                      # appending new data
                        
                        data_to_encrypt = json.dumps(useable_data).encode()             # encrypted again

                        encrypt_again = fernet.encrypt(data_to_encrypt)

                        with open(location, 'wb') as F:
                            F.write(encrypt_again)

                    else:
                        try:
                            with open(location, 'xb') as n:
                                n.write(encrypted)
                        except FileExistsError:
                            print("File already exists!")

                except ValueError:
                    print("You should only input Number!")

            elif first.lower() == 'check': 
                try:  # SYSTEM to check the passwords in a json format
                    output = input("Name of the website : ")
                    modi_output = str(output)
                        
                    try:
                        with open(location, 'rb') as f:
                            encrypted_data = f.read()
                            decrypted_data = fernet.decrypt(encrypted_data).decode() 
                            content = json.loads(decrypted_data)

                    except (FileNotFoundError, json.JSONDecodeError):
                        content = []

                    found = False

                    for item in content:
                        if item["Name of Site"].lower() == modi_output.lower():
                            agent = (item["Password"])
                            print(f"Your saved Password is : {agent}")
                            found = True
                            break

                    if not found:
                        print("The password you searched for is not in the database!")

                except ValueError:
                    print("Enter using the correct way")

            elif first.lower() == 'delete' : # Deleting a entry
                asking = input("Name of the site : ")
                asking_modi = str(asking)
                
                # system to delete an input
                file = Path(location)
                    
                if file.exists():
                    with open(location, 'rb') as f:
                        to_be_decrypted_for_deletion = f.read()
                    
                    sent_to_decrypt_for_deletion = fernet.decrypt(to_be_decrypted_for_deletion).decode()
                    useable_data_to_check = json.loads(sent_to_decrypt_for_deletion)
                    
                    for data in useable_data_to_check:
                        if data.get('Name of Site') == asking_modi:
                            useable_data_to_check.remove(data)

                    data_to_encrypt = json.dumps(useable_data_to_check).encode()

                    encrypt_again_after_delete = fernet.encrypt(data_to_encrypt)

                    with open(location, 'wb') as F:
                        F.write(encrypt_again_after_delete)
                    print("Password has been successfully deleted!")

                else:
                    print("An error occured")

            if first.lower() == 'exit':
                print('Exiting.....')
                break

        except ValueError:
            print("You should only input Number!")
