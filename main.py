MAX_LINES = 3 # creating a global variable
MAX_BET = 100
MIN_BET = 4


def depo():
    while True:
        amount = input ("AMOUNT TO DEPOSIT $:")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 20:
                return amount
            else:
                print("Amount must be greater than or equal to 20$")
        else:
            print("Please Enter a NUMBER!")
    

def get_no_lines():
    while True:
        lines = input ("Enter Number of lines you want to bet on : (1-" +str(MAX_LINES)+")? ")
        if lines.isdigit(): #to check if user input is a digit
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Lines Should be valid (1-"+ str(MAX_LINES)+")")
        else:
            print("Please Enter a NUMBER!")
    

def get_bet():
     while True:
        amount = input ("How much bet on EACH LINE $:")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} & ${MAX_BET}")
        else:
            print("Please Enter a NUMBER!")
    


def main():
    balance = depo()
    lines = get_no_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Your total bet is greater than BALANCE: {balance}")
        else:
            break
    print(f"You are betting ${total_bet} in total")
    balance = balance - total_bet
    print(f"Balance remaining: ${balance}")






main()