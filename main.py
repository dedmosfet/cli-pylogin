import hashlib
import os

rootpas = "root"
users = ["root"]
passes = []
passes.append(hashlib.md5(b"root"))

def remove_user_from_db(username):

    with open("db.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    with open("db.txt", "w", encoding="utf-8") as f:
        for line in lines:
            if line.strip():
                login, _ = line.strip().split("::")
                if login != username:
                    f.write(line)
    
    print(f"\nUser '{username}' is deleted!\n")

def user_exists(username):

    if not os.path.exists("db.txt"):
        return False
    
    with open("db.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                login, _ = line.strip().split("::")
                if login == username:
                    return True
    return False

def login():
    in_user = input("Login: ")
    
    if not user_exists(in_user):
        print("\nUser not found.")
        print("Sign up first.\n")
        return
    
    failed_attempts = 0
    max_attempts = 5
    
    while failed_attempts < max_attempts:
        in_pass = input("Password: ")
        in_hash = hashlib.md5(in_pass.encode("utf-8")).hexdigest()
        
        with open("db.txt", "r", encoding="utf-8") as f:
            logdin = False
            for line in f:
                line = line.strip()
                if line:
                    login, hash_value = line.split("::")
                    if in_user == login and in_hash == hash_value:
                        logdin = True
                        print("\nACCESS GRANTED\n")
                        print(f"Hello {login}")
                        k = input()
                        return
            
            if not logdin:
                failed_attempts += 1
                remaining = max_attempts - failed_attempts
                
                if failed_attempts < max_attempts:
                    print(f"\nACCESS DENIED")
                    print(f"Wrong passsword. Attempts left: {remaining}\n")
                else:
                    print("\nACCESS DENIED")
                    remove_user_from_db(in_user)
                    return

def main():
    option = "0"
    print("Choose your option:\n1. Login\n2. Sign up\n")
    option = input("Input number option (default 1): ")
    match option:
        case "1":
            login()
        case "2":
            signup()
        case _:
            login()

def signup():
    passin = input("Enter root password: ")
    if passin == rootpas:
        user_input = input("Enter new user login: ")
        

        if user_exists(user_input):
            print(f"User {user_input} already exists!\n")
            return
        
        pass_input = input("Enter new user password: ")
        save_pass = hashlib.md5(pass_input.encode("utf-8")).hexdigest()
        line = f"{user_input}::{save_pass}\n"
        
        with open("db.txt", "a", encoding="utf-8") as f:
            f.write(line)
        print("----------------\nNew user added: " + user_input)
    else:    
        print("Wrong root password")

main()
