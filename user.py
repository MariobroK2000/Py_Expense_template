from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "Name",
        "message": "Name of the user: ",
    },

]


# Ask which is the spender among the existing one
# Not working

def ask_user():
    users = []
    with open('users.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            users.append(row)

    users_option = {
        "type": "list",
        "name": "users_options",
        "message": "List of the users",
        "choices": [users[0], users[1], users[2]]
    }
    users_choice = prompt(users_option)

    if (users_choice['users_options']) == users[0]:
        return users[0]
    elif (users_choice['users_options']) == users[1]:
        return users[1]
    else:
        return users[2]


# Add a user in the file

def add_user():
    infos = prompt(user_questions)

    with open('users.csv', 'a', newline='') as csvfile:

        spamwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        for e in infos:
            spamwriter.writerow([infos[e]])

    print("User Added !")
    return True
