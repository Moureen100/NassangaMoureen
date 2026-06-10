#write a program for login authentication that takes a username and
#password as input and checks if they match a predefined set of credentials.
#if the credentials are correct, input "login sucessful"
#if the username is correct but the password is incorrect
#print "incorrect password".if the username is incorrect print "username not found.

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "password333":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")




    