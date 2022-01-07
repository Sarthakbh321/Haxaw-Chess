# Haxaw-Chess
A Neural Network based chess engine and GUI made with Python and Tensorflow/Keras.


## Board Representation

### Pieces

- Kings x2
- Queens x2
- Rooks x4
- Bishops x4
- Knights x4
- Pawns x16

### Extra State

- En passant
- Short castle available? x2
- Long castle available? x2

### Bitboard Composition

- Total 6 pieces of 2 colors = values upto 12 = 4 bits (12-15th bit unused)
- Extra states:
	- **each King**: 2 (castling rights)
	- **each pawn**: 1 (en passant available)
- 8x8 = 64 squares = 5 * 64 = 320 bits

### Piece encoding

**If current board state is white's turn:**

Each square will have the following values if that piece exists on it:

- Empty: 0
- King
	- White:
		- No castling possible: 1
		- Short castle possible: 2
		- Long castle possible: 3
		- Both castle possible: 4
	- Black:
		- No castling possible: 5
		- Short castle possible: 6
		- Long castle possible: 7
		- Both castle possible: 8
	
- Queens
	- White: 9 | black: 10
- Rooks
	- White: 11 | black: 12
- Bishops
	- White: 13 | black: 14
- Knights
	- White: 15 | black: 16
- Pawns
	- White: 17 | black: 18
- Is en passant square: 19


**For black's turn, all the values will be increased by 19, except 0 (which represents empty square).**
