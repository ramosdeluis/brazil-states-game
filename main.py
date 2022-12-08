from turtle import Screen
from time import sleep


from states import State
from board import Board


# from get_states_coordinates import GetCoor


screen = Screen()
screen.title('Brazil States Game')
screen.bgpic('brazil_map.gif')
screen.setup(width=720, height=736)
screen.tracer(0)

# Geting the states coordinates
# coor_one = GetCoor()
# coor_two = GetCoor()
# coor_tree = GetCoor()
# screen.listen()
# screen.onkey(coor_one.move_up, 'w')
# screen.onkey(coor_one.move_down, 's')
# screen.onkey(coor_one.move_left, 'a')
# screen.onkey(coor_one.move_right, 'd')
# screen.onkey(coor_two.move_up, 't')
# screen.onkey(coor_two.move_down, 'g')
# screen.onkey(coor_two.move_left, 'f')
# screen.onkey(coor_two.move_right, 'h')
# screen.onkey(coor_tree.move_up, 'i')
# screen.onkey(coor_tree.move_down, 'k')
# screen.onkey(coor_tree.move_left, 'j')
# screen.onkey(coor_tree.move_right, 'l')

states = State()
states.read_csv('brazil_states.csv')
board = Board()

is_game_on = True

while is_game_on:
    screen.update()
    player_state = screen.textinput('Find a Brazil state', 'State:')
    if states.write_state_name(player_state):
        board.make_point()
    if board.score == 27:
        board.end_game()
        is_game_on = False

screen.exitonclick()

# print(coor_one.position(), '   ', coor_two.position(), '   ', coor_tree.position())
