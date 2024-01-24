import random
import os

path = "moew.txt"
line = "-----------------------------------------------------------------\n"
# when we are adding path to a file in py
#  instead of c:\path we need to use
#  c:\\ path\\ sec path because of how py compiles written code


# done
def ads(pre):
    print("++++++++" + pre + "++++++++")
    os.system("cls")
    show(pre)
    target = input("name:") + "\n"
    cho = int(input("what am i doing \n1)adding\n2)deleting\n"))
    many = int(input("how many:"))
    with open(path) as file:
        l = file.readlines()
    found = False
    for i in range(len(l)):
        if l[i] == target:
            found = True
            target = i
    if found:
        with open(path, "w") as file:
            if cho == 1:
                for i in range(len(l)):
                    if i == target + 2:
                        file.write(str(int(l[i]) + many) + "\n")
                    else:
                        file.write(l[i])
            else:
                for i in range(len(l)):
                    if i == target + 2:
                        if int(l[i]) - many < 0:
                            print("not possible")
                            file.write(l[i])
                        else:
                            file.write(str(int(l[i]) - many) + "\n")
                    else:
                        file.write(l[i])
    if not found:
        print(target + "no such prodoct!!!")
        os.system("pause")


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=- =-=-=-=-=-=-=-==-=-=-=-=
# done
def add(pre):
    print("++++++++" + pre + "++++++++")
    with open(path, "a") as m:
        m.write(str(random.randint(1, 1000)) + "\n")
        m.write(input("enter product name: ") + "\n")
        m.write(input("enter product value: ") + "\n")
        m.write(input("enter products in stuck: ") + "\n")


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# done
def dele(pre):
    os.system("cls")
    print("++++++++" + pre + "++++++++")
    show(pre)
    cho = int(input("search base on id our name?\n1)id\n2)name\n"))
    if cho == 2:
        target = input("name:") + "\n"
        with open(path) as file:
            l = file.readlines()
        copy = l
        found = False
        for i in range(len(l)):
            if l[i] == target:
                found = True
                target = i
        if found:
            with open(path, "w") as file:
                for i in range(len(copy)):
                    if (
                        i != target
                        and i != target - 1
                        and i != target + 1
                        and i != target + 2
                    ):
                        file.write(copy[i])
        if not found:
            print(target + "no such product!!!")
            os.system("pause")
    else:
        target = input("id:") + "\n"
        with open(path) as file:
            l = file.readlines()
        copy = l
        found = False
        for i in range(len(l)):
            if l[i] == target:
                found = True
                target = i
        if found:
            with open(path, "w") as file:
                for i in range(len(copy)):
                    if (
                        i != target
                        and i != target + 1
                        and i != target + 3
                        and i != target + 2
                    ):
                        file.write(copy[i])
        if not found:
            print(target + "no such product!!!")
            os.system("pause")


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# done
def show(pr):
    os.system("cls")
    place_holder = 0
    with open(path) as show:
        l = show.readlines()
        for i in range(int(len(l) / 4)):
            id = l[place_holder]
            name = l[place_holder + 1]
            value = l[place_holder + 2]
            many = l[place_holder + 3]
            place_holder += 4
            printer(pre=pr, name=name, id=id, value=value, many=many)
    print("this what we all got")


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# done
def src(pre):
    os.system("cls")
    print("++++++++" + pre + "++++++++")
    place_holder = 0
    target = input("name:") + "\n"
    with open(path) as file:
        l = file.readlines()
    found = False
    for i in range(len(l)):
        if l[i] == target:
            found = True
            target = i
    if found:
        name = l[target]
        id = l[target - 1]
        value = l[target + 1]
        many = l[target + 2]
        printer(pre=pre, name=name, id=id, value=value, many=many)
        os.system("pause")
    if not found:
        print(target + "not found!!")
        os.system("pause")


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# done
def shop(name, manyi):
    target = name
    many = manyi
    with open(path) as file:
        l = file.readlines()
    found = False
    for i in range(len(l)):
        if l[i] == target:
            found = True
            target = i
    if found:
        with open(path, "w") as file:
            for i in range(len(l)):
                if i == target + 2:
                    file.write(str(int(l[i]) - many) + "\n")
                else:
                    file.write(l[i])
    if not found:
        print(target + "no such product!!!")
        os.system("pause")


# =-=-==-=-==-=-=-=-=-=-=-=-=-=-=-==-===-=-==-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-==-=-=-=-=-
def list_shop(pre):
    os.system("cls")
    print("++++++++" + pre + "++++++++")
    show(pre)
    adding = 1
    targets = []
    many = []
    while adding != 0:
        targets.append(input("pls enter product name: ") + "\n")
        many.append(int(input("pls enter how many do you want:")))
        print("you have in your list")
        for i in range(len(targets)):
            print(
                "name of product:"
                + targets[i]
                + "this many: "
                + str(many[i])
                + "\n"
                + line
            )
        cho = int(input("do you want do continue?\n1)yes\n2)no\n"))
        if cho == 2:
            adding = 0
        if adding != 0:
            os.system("cls")
            show(pre)
            for i in range(len(targets)):
                print(
                    line
                    + "name of product:"
                    + targets[i]
                    + "this many:"
                    + str(many[i])
                    + "\n"
                )
        # ==========================================
        if adding == 0:
            cho2 = int(input(line + "do you want to change any thing??\n1)yes\n2)no\n"))
            if cho2 == 1:
                ktargets = []
                kmany = []
                for i in range(len(targets)):
                    cho3 = int(
                        input(
                            line
                            + "name of product:"
                            + targets[i]
                            + "this many:"
                            + str(many[i])
                            + "\n1)edit name\n2)edit many\n3)delet this item\n4)no change\n"
                        )
                    )
                    if cho3 == 1:
                        ktargets.append(input("enter product name: ") + "\n")
                        kmany.append(many[i])
                    if cho3 == 2:
                        ktargets.append(targets[i])
                        kmany.append(int(input("enter how many you want: ")))
                    if cho3 == 3:
                        continue
                    if cho3 == 4:
                        ktargets.append(targets[i])
                        kmany.append(many[i])

            if adding == 0:
                ktargets = targets
                kmany = many
                if len(ktargets) != 0:
                    for i in range(len(ktargets)):
                        shop(name=ktargets[i], manyi=kmany[i])

                print("have nice day :-)")
            os.system("pause")


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# done
def printer(pre, name, many, value, id):
    print("***********" + pre + "***********")
    if pre == "worker" or pre == "admin":
        print("id of product:" + id)
    print("name of product:" + name)
    print("value of product:" + value)
    if many == "0\n":
        many = "out of stock!!!"
    print("products in stock:" + many)


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# done
def manu(pre):
    os.system("cls")
    if pre == "admin":
        choise = int(
            input(
                "hello admin what do you wnat\n1)adding product\n2)delet product\n3)show all\n4)search\n5)add stock\n"
            )
        )
        if choise == 1:
            add(pre)
        if choise == 2:
            dele(pre)
        if choise == 3:
            show(pre)
            os.system("pause")
        if choise == 4:
            src(pre)
            os.system("pause")
        if choise == 5:
            ads(pre)
        choise = int(input("do you want to contine??\n1)yes\n2)no\n"))
        if choise == 1:
            manu(pre)
    elif pre == "worker":
        choise = int(
            input("hello dear worker what do you want?\n1)shop\n2)show all\n3)search\n")
        )
        if choise == 1:
            list_shop(pre)
        elif choise == 2:
            show(pre)
        elif choise == 3:
            src(pre)
        choise = int(input("do you want to contine??\n1)yes\n2)no\n"))
        if choise == 1:
            manu(pre)
    else:
        os.system("cls")
        print("hi dear customer which  one do you want \n")
        list_shop(pre)
        manu(pre)


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
pre = int(
    input("\n" + line + "how is using on pc know? \n1)admin\n2)user\n3)customer\n")
)
if pre == 1:
    pre = "admin"
if pre == 2:
    pre = "worker"
if pre == 3:
    pre = "customer"
manu(pre=pre)
