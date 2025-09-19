# ██████╗ ██╗   ██╗ ██████╗ ██████╗ ██████╗    ██╗██████╗ 
# ██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗██╔══██╗   ██║██╔══██╗
# ██████╔╝ ╚████╔╝ ██║     ██║   ██║██║  ██║   ██║██████╔╝
# ██╔═══╝   ╚██╔╝  ██║     ██║   ██║██║  ██║   ██║██╔══██╗
# ██║        ██║   ╚██████╗╚██████╔╝██████╔╝██╗██║██║  ██║
# ╚═╝        ╚═╝    ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝╚═╝  ╚═╝

# تمرین 2

username = input("enter your username : ")
password = input("enter your password : ")

if username == "admin" and password == "1234":
    print("welcome!")
else:
    print("username or password is wrong !")