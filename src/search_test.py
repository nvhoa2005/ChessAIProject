import clr
import os

dll_path = os.path.abspath("ChessLib2.dll")
clr.AddReference(dll_path)


from ChessLib import Search2, Board, Move

fenn = "2r3k1/1Q4bp/1p1B1pp1/5b2/P7/6P1/1q4BP/4R2K w - - 0 1"
b = Board()
b.LoadPosition(fenn)
s = Search2(b)
time = 1000
m = s.getBestMove(time)
print("success")
print(m.Name)
