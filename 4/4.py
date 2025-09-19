# ██████╗ ██╗   ██╗ ██████╗ ██████╗ ██████╗    ██╗██████╗ 
# ██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗██╔══██╗   ██║██╔══██╗
# ██████╔╝ ╚████╔╝ ██║     ██║   ██║██║  ██║   ██║██████╔╝
# ██╔═══╝   ╚██╔╝  ██║     ██║   ██║██║  ██║   ██║██╔══██╗
# ██║        ██║   ╚██████╗╚██████╔╝██████╔╝██╗██║██║  ██║
# ╚═╝        ╚═╝    ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝╚═╝  ╚═╝

# تمرین 4


age = int(input("insert your age : "))
is_member = input("do you have a membership card? (yes/no) : ")

if age >= 18:
    if is_member.lower() == "yes":
        print("welcome to the gym!")
    else:
        print("please register as a member first !")
else:
    print("you are not old enough to register")