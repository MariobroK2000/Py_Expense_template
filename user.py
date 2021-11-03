from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "Name",
        "message": "Name of the user: ",
    },

]


def add_user():
    infos = prompt(user_questions)

    with open('users.csv', 'a', newline='') as csvfile:

        spamwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        for e in infos:
            spamwriter.writerow([infos[e]])

    print("User Added !")
    return True
