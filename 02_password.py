username = input()
password = input()

login_password = input()

while login_password != password:
    print()
    login_password = input()

print(f"Welcome {username}!")
