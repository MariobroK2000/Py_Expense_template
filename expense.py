from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "input",
        "name": "spender",
        "message": "New Expense - Spender: ",
    },

]


def new_expense(*args):
    infos = prompt(expense_questions)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as csvfile:
        expense = []
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        for e in infos:
            expense.append(infos[e])

        spamwriter.writerow([expense[0], expense[1], expense[2]])

    print("Expense Added !")
    return True
