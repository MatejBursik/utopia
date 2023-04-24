GRID_SIZE = 20

MOVEMENT = 8

coins = 0

#grid creation (not auto generated)
grid = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,6,7,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30,31,32,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,31,31,6,6,6,6,6,6,6,6,6,0,0,230,31,32,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,56,56,56,56,56,56,56,56,56,56,31,31,56,56,56,56,56,31,31,31,31,31,31,31,31,31,31,31,0,0,30,31,32,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,31,31,0,0,0,0,0,31,31,0,0,30,31,32,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,31,31,0,0,0,0,0,31,31,0,0,30,31,32,0],
[0,0,31,208,209,6,309,309,310,309,310,6,6,6,31,31,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,31,31,0,0,0,0,0,31,31,0,0,30,309,310,0],
[0,0,31,233,234,56,334,334,335,334,335,56,56,56,31,31,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,31,31,0,0,0,0,0,31,31,0,0,30,334,335,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,6,6,6,6,6,6,6,6,31,31,6,6,6,6,6,6,6,31,31,6,6,6,0,0,31,31,0,0,30,31,32,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,31,31,0,0,31,31,0,0,30,31,32,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,31,31,0,0,30,31,32,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,31,31,0,0,30,309,310,0],
[0,31,31,31,6,6,6,6,6,6,6,6,6,6,31,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,31,31,0,0,30,334,335,0],
[0,56,56,56,56,56,56,56,10,8,56,56,56,56,31,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,23,21,0,0,31,31,31,31,31,31,32,0],
[0,0,0,0,0,0,0,0,30,32,0,0,0,0,31,31,31,31,31,31,71,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,73,46,0,0,31,31,31,31,31,31,32,0],
[0,0,0,0,0,0,0,0,30,32,0,0,0,0,56,56,56,56,56,56,21,23,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,46,0,0,0,0,0,0,31,31,0,0],
[0,0,0,0,0,0,0,0,30,32,0,0,0,0,0,0,0,0,0,0,0,48,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,46,0,0,0,0,0,0,31,31,0,0],
[0,0,0,0,0,0,0,0,30,32,0,0,0,0,0,0,0,0,0,0,0,48,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,46,0,0,0,0,0,0,31,31,0,0],
[0,5,6,6,6,6,6,6,31,32,0,0,0,0,0,0,0,0,0,0,0,48,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,46,0,0,0,0,0,0,31,31,0,0],
[0,30,31,31,31,31,31,31,31,32,0,0,0,0,0,0,0,0,0,0,0,48,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,71,333,309,310,31,31,31,31,31,31,0],
[0,30,31,0,0,0,0,0,35,32,0,0,0,0,0,0,0,0,0,0,0,48,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,21,286,334,335,31,31,31,31,31,31,0],
[0,30,31,0,0,0,0,0,35,32,0,0,0,0,0,0,0,0,0,0,0,48,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,46,0,0,0,31,31,0,0,0,0,0],
[0,30,31,0,0,0,0,0,35,32,0,0,0,0,0,0,0,0,0,0,0,48,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,46,0,0,0,31,31,0,0,0,0,0],
[0,30,31,0,0,0,0,0,35,32,0,0,0,0,0,0,0,0,0,0,0,48,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,46,0,0,0,31,31,0,0,0,0,0],
[0,30,31,0,0,0,0,0,35,58,6,6,6,6,6,6,6,6,6,71,19,73,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,46,0,0,0,31,31,0,0,0,0,0],
[0,30,31,6,6,6,6,6,60,8,56,56,56,56,31,31,31,31,31,21,69,22,22,22,22,22,22,22,22,22,22,22,22,22,22,23,21,22,22,46,0,0,31,31,31,6,6,6,32,0],
[0,55,56,56,56,56,56,56,56,57,0,0,0,0,31,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,73,71,0,0,0,0,0,31,31,8,10,31,31,32,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,80,80,0,0,0,0,0,31,31,31,8,60,31,32,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,58,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30,80,0,0,0,0,0,31,31,9,31,58,31,32,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30,32,0,0,0,0,0,31,31,60,60,31,31,32,0],
[0,0,0,0,0,0,0,0,0,0,0,0,5,6,31,31,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0,0,30,32,0,0,83,83,30,31,31,31,31,31,31,32,0],
[0,0,6,6,6,6,6,6,6,6,6,6,60,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,0,0,30,32,0,0,83,56,31,31,31,31,31,31,31,32,0],
[0,0,31,31,31,31,31,31,31,31,31,31,31,31,31,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,31,31,0,0,30,32,0,0,0,0,0,0,31,31,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,31,31,0,0,30,32,0,0,0,0,0,0,31,31,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,0,0,0,30,32,0,0,0,0,0,0,31,31,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,0,0,0,30,32,0,0,0,0,0,0,31,31,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,333,31,3221225757,31,31,285,31,286,0,0,6,6,0,0,0,0,0,0,30,58,6,6,6,6,6,6,31,31,6,6,6,7,0],
[0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,31,31,31,31,31,31,31,31,31,31,31,31,0,0,0,0,0,0,30,8,56,56,10,31,8,31,10,58,60,60,31,32,0],
[0,0,0,0,0,0,0,0,31,31,31,31,31,31,31,31,31,31,60,58,60,58,58,10,31,31,31,31,31,31,31,31,31,0,0,30,32,0,0,35,31,58,10,58,60,8,60,31,32,0],
[0,0,0,0,0,0,0,0,31,31,31,0,0,0,0,0,31,31,31,8,60,31,31,31,31,31,31,31,31,31,31,31,31,0,0,30,32,0,0,35,8,56,56,10,8,56,56,10,32,0],
[0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,0,0,0,30,32,0,0,35,33,0,0,55,57,0,0,30,32,0],
[0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,0,0,0,30,32,0,0,35,33,0,0,156,157,0,0,30,32,0],
[0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30,32,0,0,55,57,0,0,181,182,0,0,55,57,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30,32,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,60,32,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,57,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

GRID_WIDTH = len(grid[0]) * GRID_SIZE
GRID_HEIGHT = len(grid) * GRID_SIZE

# window width and height
WIDTH = int((len(grid[0]) * 1.5) * GRID_SIZE)
HEIGHT = int(len(grid) * GRID_SIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_GRAY = (20,20,18)
TERM_GRAY = (10,10,9)

GAME_NAME = "Utopia"

# text field history
command_history = [""]
command_index = 0

# zoom factor
ZOOM = 4

CHANGE_THRESHOLD = 0.1

# zoom implementation
def zoomify(_number):
    # i guess 500 was magic, who knew
    return ZOOM*_number+500
