🏏 Hand Cricket Game
A command-line implementation of the classic Hand Cricket game using Python. Play against the computer in a fun and interactive way!

🎮 Game Features
Toss Mechanism: Choose between "ODD" or "EVEN" to decide who bats or bowls first.

Interactive Gameplay: Input numbers between 0 to 6 to play your turn.

Two Innings: Both player and computer get a chance to bat and bowl.

Score Tracking: Real-time display of scores and outcomes.

Replay Option: Play multiple rounds without restarting the program.

🛠️ Prerequisites
Python 3.x installed on your system.

🚀 How to Run
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/yourusername/hand-cricket-game.git
cd hand-cricket-game
Run the Game:

bash
Copy
Edit
python hand_cricket.py
Note: Replace hand_cricket.py with the actual filename if different.

📄 Game Rules

*Toss:

Choose "ODD" or "EVEN".

Both player and computer select a number between 0 to 6.

Sum determines the winner of the toss.

* Gameplay:

Batting: Input a number between 0 to 6.

Bowling: Computer randomly selects a number between 0 to 6.

If both numbers match, the batsman is out.

Continue until out, then switch roles.

* Winning:

The player with the higher score after both innings wins.

In case of a tie, the match is declared as tied.

🧑‍💻 Code Overview
Functions:

h_bat(scorer, s): Handles the batting logic.

h_bowl(scoreh, s): Handles the bowling logic.

Main Loop:

Manages the game flow, including toss, innings, and replay options.

🧑‍💻 AUTHOR
M>Logeshwaran , CSE student , beginner
