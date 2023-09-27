import math
import random


# def database(user_name, age, YOB):
#     verified = False
#     num_of_post = 4
#     Id = random.randrange(1, 999, 1)
#     credentials_bio = [user_name, age, YOB]
#     generated = {"num_of_post": num_of_post, "id": Id, "verified": verified}
#     return {
#         "credentials_bio": credentials_bio,
#         "system_generated": generated
#     }
#
#
# def server(user_name, age, YOB):
#     data = database(user_name, age, YOB=YOB)
#     return data
#
#
# def user_client():
#     send_name = input("enter your name ")
#     send_age = input("enter your age ")
#     send_yr_of_birth = input("enter birth date ")
#     re_list = []
#     responds = server(send_name, send_age, send_yr_of_birth)
#     for add in responds.get("credentials_bio"):
#         re_list.append(add)
#     re_list.append(responds.get("system_generated"))
#     return {
#         "sent Data": [send_name, send_age, send_yr_of_birth],
#         "received data from server": re_list
#     }
#
#
# print(user_client())
#

# deep crud operation
def database(user_name, age, YOB):
    verified = False
    num_of_post = 4
    Id = random.randrange(1, 999, 1)
    credentials_bio = [user_name, age, YOB]
    generated = {"num_of_post": num_of_post, "id": Id, "verified": verified}
    return {
        "credentials_bio": credentials_bio,
        "system_generated": generated
    }


def server(user_name, age, YOB, ):
    data = database(user_name, age, YOB=YOB)
    return data


def user_client(type_of):
    def loop(respond_text):
        for add in respond_text.get("system_generated"):
            edit_account.append(add)
        re_list.append(respond_text.get("credentials_bio"))

    default_values = ("Newbie", 23, 1997)
    N, A, YOB = default_values
    edit_account = []
    re_list = []
    split_all = type_of.split(' ')
    default = server(N, A, YOB)

    if type_of == 'sign up':
        send_name = input("enter your name ")
        send_age = input("enter your age ")
        send_yr_of_birth = input("enter birth date ")

        responds = server(send_name, send_age, send_yr_of_birth)
        for add in responds.get("credentials_bio"):
            re_list.append(add)
        re_list.append(responds.get("system_generated"))
    elif "edit" in split_all:

        if "read" in split_all:
            respond_text = server(N, A, YOB)
            edit_account.append(respond_text.get("system_generated"))
            re_list.append(respond_text.get("credentials_bio"))
        elif "create" in split_all:
            send_name = input("enter your name ")
            send_age = input("enter your age ")
            send_yr_of_birth = input("enter birth date ")
            respond_text = server(send_name, send_age, send_yr_of_birth)
            for add in respond_text.get("system_generated"):
                re_list.append(respond_text.get("credentials_bio"))
                edit_account.append(add)
            re_list.append(respond_text.get("credentials_bio"))

        elif "update" in split_all:
            send_name = input("change your name ")
            send_age = input("change your age ")
            send_yr_of_birth = input("change birth date ")
            respond_text = server(send_name, send_age, send_yr_of_birth)
            for add in respond_text.get("system_generated"):
                edit_account.append(add)

        elif "delete" in split_all:
            remove_what = input("what do you want to remove").lower()
            if remove_what == "name":
                default.pop(remove_what)
                loop(default)
            elif remove_what == "age":
                default.pop(remove_what)
                loop(default)
            elif remove_what == "year of birth":
                default.pop(remove_what)
                loop(default)
            else:
                print("sorry, enter a valid input")

    return {
        "edit_account": edit_account,
        "re_list": re_list
    }


type_of_operation = input("sign up or edit account and run crud(edit and read)").lower()
print(user_client(type_of_operation))
