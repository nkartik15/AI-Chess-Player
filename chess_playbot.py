# -*- coding: utf-8 -*-
"""
AI Chess Player with Visual Board
@author: Kartik
"""

from stockfish import Stockfish
import chess
from chessboard import display

# ✅ Set your Stockfish executable path
engine_path = r"C:\Stockfish\stockfish-windows-x86-64-avx2.exe"
engine = Stockfish(path=engine_path)
print("✅ Stockfish engine loaded successfully!")

# Create a new chess board
board = chess.Board()

# Create visual board window
board_window = display.start()

while not board.is_game_over():
    display.update(board_window, board.fen())

    print(board)
    print("\nYour move (e.g., e2e4): ", end="")
    move = input().strip()

    try:
        user_move = chess.Move.from_uci(move)
        if user_move not in board.legal_moves:
            print("❌ Illegal move. Try again.\n")
            continue
        board.push(user_move)
    except:
        print("⚠️ Invalid input format! Try again (example: e2e4)\n")
        continue

    # Update display after player's move
    display.update(board_window, board.fen())

    # Check if the game ended after player's move
    if board.is_game_over():
        break

    # Stockfish calculates best move
    engine.set_fen_position(board.fen())
    ai_move = engine.get_best_move()
    print(f"\n🤖 Stockfish plays: {ai_move}\n")

    # Apply AI move
    board.push(chess.Move.from_uci(ai_move))

# Game over message
display.update(board_window, board.fen())
print("\n🏁 Game Over!")
print("Result:", board.result())

# Keep window open until you close it
display.terminate()
