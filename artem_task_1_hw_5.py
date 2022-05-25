# get data of user
password: str = input()
if password != "":
    # check  matching first password with second password
    check_password: str = input("Enter your password again")
    #  if password matched
    if password == check_password:
        print("Your password was accepted ")
    #  if password did not match
    else:
        print("Sorry your password is different ")
# if our password empty
else:
    print("Please enter your password   ")
