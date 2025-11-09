 ♟️ AI Chess Player

 🚀 Project Overview  
This project implements a **Python-based AI Chess Engine** that allows a user to play against the powerful **Stockfish engine**.  
It integrates the **Minimax Algorithm with Alpha-Beta Pruning** for intelligent decision-making and includes a **visual chessboard interface** for real-time move visualization.  
The game provides an engaging, human-vs-AI chess experience with instant AI responses and move validation.


 🧩 Key Features

🧠 AI-Powered Gameplay  
Utilizes the **Minimax Algorithm with Alpha-Beta Pruning** to simulate strategic, human-like AI decision-making.

⚙️ Stockfish Integration  
Integrates the open-source **Stockfish Engine** for powerful move computation and realistic gameplay.

🖥️ Visual Interface  
Displays a live chessboard using **Pygame** or the **chessboard** Python library. The board updates automatically after each move.

♟️ Player vs Computer Mode  
Allows the player to make moves in **UCI format** (e.g., `e2e4`) and watch Stockfish counter in real-time.

🔢 Game Logic & Validation  
Implements legal move checking, position updates, and detects endgame states such as checkmate, stalemate, or draw.


 🧠 System Workflow

1. Initialize Engine: Connect to the Stockfish executable.  
2. Create Board: Set up a new chessboard using `python-chess`.  
3. Player Move: Accept and validate user input.  
4. AI Response: Stockfish computes the best move instantly.  
5. Display: Visual interface updates after every move.  
6. Game Over: Displays final board and result (`1-0`, `0-1`, or `½-½`).


 ⚙️ Tech Stack

| Category | Tools / Technologies |
|-----------|----------------------|
| Language | Python |
| AI Engine | Stockfish |
| Logic Library | `python-chess` |
| Visualization | `chessboard`, `pygame` |
| Algorithm | Minimax with Alpha-Beta Pruning |


 🧩 Installation & Setup

 1️⃣ Install Dependencies
'termminalop' 
pip install stockfish python-chess pygame chessboard
