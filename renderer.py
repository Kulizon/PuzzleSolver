import pygame

# stałe dla kolorów
white = (255, 255, 255)
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (128, 0, 0), (0, 128, 0), (0, 0, 128),
    (128, 128, 0), (128, 0, 128), (0, 128, 128),
    (255, 128, 0), (255, 0, 128), (128, 255, 0),
    (128, 0, 255), (0, 128, 255), (255, 128, 128),
    (128, 255, 128), (128, 128, 255)
]

# zmienna określająca szerokość boku kwadratu składającego się na każdy element
rect_size = 10


def setup_window(window_width, window_height, given_rect_size):
    global rect_size
    rect_size = given_rect_size
    return pygame.display.set_mode([window_width, window_height])

def render_board(screen, solved_matrix):
    window_width, window_height = pygame.display.get_surface().get_size()

    board_height = rect_size * len(solved_matrix)
    board_width = rect_size * len(solved_matrix[0])

    # wyśrodkuj planszę
    offset_x = (window_width - board_width) / 2
    offset_y = 25

    # tło planszy, gdzie układane są elementy
    board_rect = (offset_x, offset_y, board_width, board_height)
    pygame.draw.rect(screen, (225, 225, 225), board_rect)

    # rysowanie już ułożonych elementów na planszy
    for row_index, row in enumerate(solved_matrix):
        for col_index, value in enumerate(row):
            rect_to_draw = (col_index * rect_size + offset_x, row_index * rect_size + offset_y, rect_size, rect_size)
            if value != 0:
                pygame.draw.rect(screen, colors[value], rect_to_draw)

    # długość planszy na ekranie dla późniejszego rysowania pozostałych elementów
    board_height = board_height + offset_y
    return board_height


def render_pieces(screen, number_matrices, board_offset_y):
    window_width, window_height = pygame.display.get_surface().get_size()

    # zmienne do wyznaczania odległości między sąsiednimi elementami
    offset_x = 0
    offset_y = 0

    all_pieces_offset_x = 25
    all_pieces_offset_y = board_offset_y + 55

    # przestrzeń między elementami obok siebie i pod sobą
    grid_gap = 10

    # zmienna do późniejszego wyznaczania offset_y - aby elementy w rzędach na siebie nie nachodziły
    max_row_elem_height = 0

    # rysowanie wszystkich elementów w siatce pod planszą
    for number, matrix in number_matrices.items():
        max_row_elem_height = max(max_row_elem_height, len(matrix))

        for row_index, row in enumerate(matrix):

            # jeśli ma wyjść poza ekran - zacznij od nowego rzędu
            if offset_x + len(row) * rect_size + 25 > window_width:
                offset_x = 0
                offset_y = offset_y + (max_row_elem_height * rect_size + grid_gap)
                max_row_elem_height = 0

            # rysowanie pojedycznego elementu
            for col_index, value in enumerate(row):
                if value != 0:

                    total_offset_x = offset_x + all_pieces_offset_x
                    total_offset_y = offset_y + all_pieces_offset_y
                    pos_x, pos_y = calc_piece_pos(row_index, col_index, total_offset_x, total_offset_y)

                    rect_to_draw = (pos_x, pos_y, rect_size, rect_size)
                    pygame.draw.rect(screen, colors[number], rect_to_draw)

        # odleglość dla następnego elementu, zależna od aktualnego elementu
        offset_x = offset_x + len(matrix[0]) * (rect_size + 5)

    return offset_y


def calc_piece_pos(row_index, col_index, offset_x, offset_y):
    pos_x = col_index * rect_size + offset_x
    pos_y = row_index * rect_size + offset_y

    return pos_x, pos_y


def render_background(screen):
    screen.fill(white)


def render_success_message(screen, board_offset_y):
    font = pygame.font.Font(None, 36)

    success_text = font.render("Udało się!", True, (255, 255, 255))
    text_rect = success_text.get_rect(center=(screen.get_width() // 2, board_offset_y + 50))

    padding = 20

    pygame.draw.rect(screen, (0, 200, 0), (text_rect.x - padding/2, text_rect.y - padding/2, text_rect.width + padding, text_rect.height + padding))
    screen.blit(success_text, text_rect)



