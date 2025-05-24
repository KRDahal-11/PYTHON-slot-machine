
import random 

MAX_LINES = 3 # creating a global variable
MAX_BET = 100
MIN_BET = 4

ROWS = 3
COLS= 3

symbol_count = { # no of digits present for each symbol
    "A" : 3,
    "B" : 4,
    "C" : 5,
    "D" : 6
}

symbol_value = { # value won by getting each symbol 3 in a row
    "A" : 6,
    "B" : 5,
    "C" : 3,
    "D" : 2
}

def slot_spin(rows, cols, symbols):
    all_symbols = [] # created a list for all possible symbols
    for symbol, symbol_count in symbols.items(): # symbol--> A,B,C,D symbol_count-->2,3,4,5
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # the : helps to copy all_symbols to current_symbols
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) #removes the symbol just obtained from the list
            column.append(value)
            
        columns.append(column)

    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i !=len(columns) -1:
                print(column[row], end=" | " )
            else:
                print(column[row], end="")
        print() # prints new line like \n after a row



def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else: # else for - for loop - ??
            winnings += values[symbol] * bet
            winning_line.append(line+1)

    return winnings, winning_line
    



            

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
    
def game(balance):
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

    slots = slot_spin(ROWS , COLS , symbol_count)
    print_slot(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet , symbol_value)
    print(f"you won ${winnings}")
    print(f"You won on lines: ", *winning_lines )
    return winnings - total_bet


def main():
    balance = depo()
    while True:
        print(f"Current balance is ${balance}")
        reply= input("Press enter to spin.(q to quit)")
        if reply == "q":
            break
        balance += game(balance)
    
main()