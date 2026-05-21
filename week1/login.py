user="admin"
psw="1234"

input_user = input("Enter username: ")
input_psw = input("Enter password: ")   

if input_user == user and input_psw == psw:
    print("Login successful!")
else:
    print("Login failed. Please check your username and password.")
    