import clr
import os

dll_path = os.path.join(os.path.dirname(__file__), "ChessLib.dll")
clr.AddReference(dll_path)

from ChessLib import Evaluation

e = Evaluation()
print(dir(e))
fenn = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
print(str(e.EvaluateBoard(fenn)))  # or call a method if it has one
