import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input('what amount would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('please enter a value greater than zero')
        else:
            print('Enter a valid number')
    return amount


def get_number_of_lines():
    while True:
        lines = input(f'Enter number of lines you wanna bet 1-{MAX_LINE}? ')
        if lines.isdigit():
            line = int(lines)
            if 1 <= line <= MAX_LINE:
                break
            else:
                print(f'Enter a valid number 1-{MAX_LINE}')
        else:
            print('Enter a number ')
    return line


def get_bet():
    while True:
        amount = input('How much money do you wanna bet on each line? $')
        if amount.isdigit():
            bet = int(amount)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Enter a value  between {MAX_BET} -{MIN_BET}')
        else:
            print('Enter a valid number')
    return bet


ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8

}


def get_slot_machine(row, col, symbol):
    all_symbol = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)
    columns = []
    for _ in range(col):
        column = []
        current_symbol = all_symbol[:]
        for _ in range(row):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns):
                print(column[row], end='|')
            else:
                print(column[row])

        print()


def check_win(columns, lines, bet, value):
    win = 0
    for line in range(lines):
        symbol = columns[0][lines]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            win += value[symbol] * bet
    return win


def main():
    balance = deposit()
    while True:
        line = get_number_of_lines()
        while True:
            bet = get_bet()
            total_bet = bet * line
            if total_bet > balance:
                print(f'insufficient balance you have ${balance}')
            else:
                break
        print(f"you want to bet ${bet} on {line} lines: your total bet is ${total_bet}")
        slot = get_slot_machine(ROWS, COLS, symbol_count)
        print_slot_machine(slot)
        wins = check_win(slot, line, bet, symbol_count)
        print(f'you won ${wins}')
        if wins > 0:
         break


main()
