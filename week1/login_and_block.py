for i in range(0,3):
    us=input("Enter your username")
    ps=input("Enter your password")
    if us=="admin" and ps=="admin123":
        print("Login successful")
          
    else:
        print("Login failed")
print("Your account is blocked for 24 hours")