from load_data import *
from solver import *
from renderer import *
import copy

def pretty_print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:4}", end=" ")  # Adjust the width as needed
        print()

# wczytanie argumentów wywołania
file_path_full_board, file_path_board_to_solve, moves_delay, width, height, rect_size = parse_arguments()

# wyfiltrowanie elementów, które są do ułożenia na podstawie całkowicie ułożonej planszy
number_matrices = filter_out_elements_to_use(file_path_full_board, file_path_board_to_solve)

# zapisanie oryginalnych, niewstawionych elementów planszy
original_number_matrices = dict(number_matrices)

# inicjalizacja ułożonej macierzy
original_solved_matrix = read_matrix_from_file(file_path_board_to_solve)
solved_matrix = copy.deepcopy(original_solved_matrix)


pygame.init()
pygame.display.set_caption("Układator puzzli")

screen = setup_window(width, height, rect_size)
start_time = pygame.time.get_ticks()

running = True
isSolved = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    if elapsed_time >= moves_delay and not isSolved:
        start_time = current_time
        added = put_any_piece_on_board(number_matrices, solved_matrix)

        if not added:
            if len(number_matrices.keys()) == 0:
                isSolved = True
            else:
                solved_matrix = copy.deepcopy(original_solved_matrix)
                number_matrices = dict(original_number_matrices)

    if isSolved and elapsed_time >= 10000:
        running = False

    render_background(screen)
    board_offset_y = render_board(screen, solved_matrix)
    render_pieces(screen, number_matrices, board_offset_y)

    if isSolved:
        render_success_message(screen, board_offset_y)

    pygame.display.flip()


pygame.quit()
