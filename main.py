MAX_LINES = 3 # creating a global variable
MAX_BET = 100
MIN_BET = 4


def depo():
    while True:
        amount = input ("AMOUNT TO DEPOSIT $:")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 20:
                break
            else:
                print("Amount must be greater than or equal to 20$")
        else:
            print("Please Enter a NUMBER!")
    return amount

def get_no_lines():
    while True:
        lines = input ("Enter Number of lines you want to bet on : (1-" +str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines Should be valid (1-"+ str(MAX_LINES)+")")
        else:
            print("Please Enter a NUMBER!")
    return lines


    


def main():
    balance = depo()
    lines = get_no_lines()
    print(balance ,  lines)




main()