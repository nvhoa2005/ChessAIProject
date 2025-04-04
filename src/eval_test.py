import clr
import os

dll_path = os.path.abspath("../../csharp/ChessLib/bin/Debug/net6.0/ChessLib.dll")
clr.AddReference(dll_path)

from ChessLib import Evaluation

e = Evaluation()
print(str(e.EvaluateBoard("LMAO")))  # or call a method if it has one
