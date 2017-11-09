"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.
But we will not be playing this game. You will be the referee for this games results. You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
x-o-referee
A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.
Input: A game result as a list of strings (unicode) like ["X.O","XX.","XOO"].
Output: "X", "O" or "D" as a string.
Precondition:
There is either one winner or a draw.
len(game_result) == 3
all(len(row) == 3 for row in game_result)
"""

def checkio(game_result):
    resultado = separar(game_result)
    return conditions(resultado)
    
def separar(lista):
  lista_final=[]
  for cadena in lista:
    for ch in cadena:
      lista_final.append(ch)
  return lista_final

def conditions(res):
    if res[0] == res[1] == res[2] and res[0] != '.':
        return res[0]
    if res[0] == res[3] == res[6] and res[0] != '.':
        return res[0]
    if res[0] == res[4] == res[8] and res[0] != '.':
        return res[0]
    if res[1] == res[4] == res[7] and res[1] != '.':
        return res[1]
    if res[2] == res[5] == res[8] and res[2] != '.':
        return res[2]
    if res[3] == res[4] == res[5] and res[3] != '.':
        return res[3]
    if res[6] == res[7] == res[8] and res[6] != '.':
        return res[6]
    if res[2] == res[4] == res[6] and res[6] != '.':
        return res[6]
    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

