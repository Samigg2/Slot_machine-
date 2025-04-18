🎰 Slot Machine Game (Python CLI)

This is a simple command-line slot machine game written in Python. 
It allows users to deposit money, place bets on lines, spin the 
slot machine, and potentially win based on matching symbols.


🧠 How It Works
The player deposits money.

Chooses how many lines (up to 3) to bet on.

Places a bet per line.

A random 3x3 grid of symbols is generated to simulate a slot machine.

If the symbols in any of the bet lines match, the player wins money based on the symbol's value.


💡 Features

User input validation.

Configurable betting range.

Symbol-based winning logic.

Randomized 3x3 slot machine grid.

Clear and user-friendly terminal outputs.

🛠️ Game Configuration

python
Copy
Edit
MAX_LINE = 3       # Maximum number of lines to bet on
MAX_BET = 100      # Maximum bet per line
MIN_BET = 1        # Minimum bet per line

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

🔄 Game Flow

Deposit funds
Prompted to enter an amount to start with.

Choose lines to bet
Choose between 1 to 3 lines.

Place bet per line
Input how much to bet on each line within the allowed range.

Spin the slot machine
A 3x3 grid of symbols is generated based on predefined probabilities.

Check for wins
If the same symbol appears across a selected line, the winnings are calculated.

Play again or end
The game continues if there's enough balance unless the player wins.

📦 How to Run

Make sure Python is installed on your system, then:

bash
Copy
Edit
python slot_machine.py
Replace slot_machine.py with your file name.

🚧 Known Issues
The win calculation uses symbol_count as a value multiplier, which might be confusing. You may want to separate symbol frequency and symbol payout values for clarity.

There's no loop to continue the game after a win or a loss — it stops after the first win.

✅ To Do
Add replay functionality (ask user if they want to play again).

Track total balance after each round.

Create a better symbol payout system.

Add color or improve formatting for better UX.

🤝 Contributing
Feel free to fork the repo and submit pull requests if you have improvements or fixes.
