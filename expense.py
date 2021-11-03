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
    {
        "type": "input",
        "name": "people",
        "message": "New Expense - People involved: ",
    },

]


def new_expense_test(amount, label, spender):
    infos = prompt(expense_questions)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as csvfile:
        expense = []
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        for e in infos:
            expense.append(infos[e])

        if not (amount.isnumeric()):
            print("Amount can't be letters, please try again")
            return False

        if not (label.isalpha()):
            print("Label can't be numbers, please try again")
            return False

        if not (spender.isalpha()):
            print("Spender can't be numbers, please try again")
            return False

        if not (expense[3].isalpha()):
            print("People can't be numbers, please try again")
            return False

        spamwriter.writerow([expense[0], expense[1], expense[2], expense[3]])

    print("Expense Added !")
    return True


def new_expense(*args):
    infos = prompt(expense_questions)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as csvfile:
        expense = []
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        for e in infos:
            expense.append(infos[e])

        if not (expense[0].isnumeric()):
            print("Amount can't be letters, please try again")
            return False

        if not (expense[1].isalpha()):
            print("Label can't be numbers, please try again")
            return False

        if not (expense[2].isalpha()):
            print("Spender can't be numbers, please try again")
            return False

        if not (expense[3].isalpha()):
            print("People can't be numbers, please try again")
            return False

        spamwriter.writerow([expense[0], expense[1], expense[2], expense[3]])

    print("Expense Added !")
    return True
