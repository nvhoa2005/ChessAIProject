# Caption
GAME_NAME = "Chess"

# Screen
WIDTH = 800
HEIGHT = 800

# Board
COLS = 8
ROWS = 8
SQUARE_SIZE = WIDTH // COLS

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# fps
FPS = 25

# sound_rect
SOUND_RECT = (WIDTH-120, 10, 120, 110)

# choice
PVP = 1
AI = 2
CONTINUE = 3
RESTART = 4
QUIT = 0

# status
RUNNING = 2
WHITEWON = 4
BLACKWON = 5

# theme
GREEN = (234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), '#C86464', '#C84646'
BROWN = (235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), '#C86464', '#C84646'
BLUE = (229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), '#C86464', '#C84646'
GRAY = (120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128), '#C86464', '#C84646'

# pause type (thắng, thua, dừng gọi chung là pause)
BLACK_WIN = 100
WHITE_WIN = 200
PAUSED_GAME = 300
DRAW = 150

# Piece
KING_NAME = "king"
QUEEN_NAME = "queen"
ROOK_NAME = "rook"
BISHOP_NAME = "bishop"
KNIGHT_NAME = "knight"
PAWN_NAME = "pawn"

WHITE_KING = "white_king"
BLACK_KING = "black_king"
WHITE_QUEEN = "white_queen"
BLACK_QUEEN = "black_queen"
WHITE_ROOK = "white_rook"
BLACK_ROOK = "black_rook"
WHITE_BISHOP = "white_bishop"
BLACK_BISHOP = "black_bishop"
WHITE_KNIGHT = "white_knight"
BLACK_KNIGHT = "black_knight"
WHITE_PAWN = "white_pawn"
BLACK_PAWN = "black_pawn"

# Piece color
WHITE_PIECE = "white"
BLACK_PIECE = "black"

# Player
WHITE_PLAYER = "white"
BLACK_PLAYER = "black"

# Sound
CAPTURE = "capture"
MOVE = "move"

# Font
FONT_GAME = "monospace"

# Text
PAUSED_TEXT = "PAUSED"
WHITE_WIN_TEXT = "WHITE WIN"
BLACK_WIN_TEXT = "BLACK WIN"
DRAW_TEXT = "DRAW"

# Other
SELECT_MODE = "Select mode"
HOVER = "hover"
CLICK = "click"

(
    EMPTY,
    PAWN,
    KNIGHT,
    BISHOP,
    ROOK,
    QUEEN,
    KING,
    HAWK,
    ELEPHANT,
    BPAWN,
    ASEAN_WBISHOP,
    ASEAN_BBISHOP,
    ASEAN_QUEEN,
) = range(13)

# Castling values
W_OO, W_OOO, B_OO, B_OOO = (2**i for i in range(4))