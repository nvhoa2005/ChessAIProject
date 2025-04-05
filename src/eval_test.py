import clr
import os

dll_path = os.path.abspath("../../csharp/ChessLib/bin/Debug/net6.0/ChessLib.dll")
clr.AddReference(dll_path)

from ChessLib import Evaluation

e = Evaluation()

fenn = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
print(str(e.EvaluateBoard(fenn)))  # or call a method if it has one
