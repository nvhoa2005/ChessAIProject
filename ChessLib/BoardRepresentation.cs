﻿namespace ChessLib {

	public static class BoardRepresentation {
		public const string fileNames = "abcdefgh";
		public const string rankNames = "12345678";

		public const int a1 = 0;
		public const int b1 = 1;
		public const int c1 = 2;
		public const int d1 = 3;
		public const int e1 = 4;
		public const int f1 = 5;
		public const int g1 = 6;
		public const int h1 = 7;

		public const int a8 = 56;
		public const int b8 = 57;
		public const int c8 = 58;
		public const int d8 = 59;
		public const int e8 = 60;
		public const int f8 = 61;
		public const int g8 = 62;
		public const int h8 = 63;

		// Rank (0 to 7) of square 
		public static int RankIndex (int squareIndex) {
			return squareIndex >> 3;
		}

		// File (0 to 7) of square 
		public static int FileIndex (int squareIndex) {
			return squareIndex & 0b000111;
		}

		public static int IndexFromCoord (int fileIndex, int rankIndex) {
			return rankIndex * 8 + fileIndex;
		}

		public static int IndexFromCoord (Coord coord) {
			return IndexFromCoord (coord.fileIndex, coord.rankIndex);
		}

		public static Coord CoordFromIndex (int squareIndex) {
			return new Coord (FileIndex (squareIndex), RankIndex (squareIndex));
		}

		public static bool LightSquare (int fileIndex, int rankIndex) {
			return (fileIndex + rankIndex) % 2 != 0;
		}

		public static string SquareNameFromCoordinate (int fileIndex, int rankIndex) {
			return fileNames[fileIndex] + "" + (rankIndex + 1);
		}

		public static string SquareNameFromIndex (int squareIndex) {
			return SquareNameFromCoordinate (CoordFromIndex (squareIndex));
		}

		public static string SquareNameFromCoordinate (Coord coord) {
			return SquareNameFromCoordinate (coord.fileIndex, coord.rankIndex);
		}
	}
}