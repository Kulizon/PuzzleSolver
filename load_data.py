import argparse
from matrix_utility import *

def pretty_print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:4}", end=" ")  # Adjust the width as needed
        print()


def get_matrix_dimensions(file_path):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            height = int(line.split(" ")[0])
            width = int(line.split(" ")[1])

            return width, height

def read_matrix_from_file(file_path):
    matrix = []

    with open(file_path, 'r') as file:
        for k, line in enumerate(file):
            # pomiń pierwszy wiersz z wymiarami macierzy
            if k == 0:
                continue

            numbers = list(map(int, line.split()))
            matrix.append(numbers)

    return matrix

def load_matrices_from_file(file_path):
    number_matrices = {}

    num_elem_x, num_elem_y = get_matrix_dimensions(file_path)

    with open(file_path, 'r') as file:
        for k, line in enumerate(file):
            # pomiń pierwszy wiersz z wymiarami macierzy
            if k == 0:
                continue
            i = k-1

            numbers = list(map(int, line.split()))
            for j, number in enumerate(numbers):
                if number not in number_matrices:
                    number_matrices[number] = [[0 for _ in range(num_elem_x)] for _ in range(num_elem_y)]

                number_matrices[number][i][j] = number

    return number_matrices


def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do układania puzzli.')

    parser.add_argument('-p', '--ulozona_plansza', default='plansza.txt', help='Plik z ułożoną planszą')
    parser.add_argument('-n', '--czas', type=float, default=1, help='Czas w sekundach między kolejnymi ruchami')
    parser.add_argument('-s', '--szerokosc', type=int, default=960, help='Szerokość okna w pikselach')
    parser.add_argument('-w', '--wysokosc', type=int, default=600, help='Wysokość okna w pikselach')
    parser.add_argument('-b', '--bok', type=int, default=30, help='Długość boku kwadratu składającego się na element w pikselach')
    parser.add_argument('plansza', help='Plik z planszą do ułożenia')

    args = parser.parse_args()

    return args.ulozona_plansza, args.plansza, args.czas * 1000, args.szerokosc, args.wysokosc, args.bok


def filter_out_elements_to_use(file_path_full_board, file_path_board_to_solve):
    # wczytanie wszystkich elementów z ułożonej planszy
    full_number_matrices = load_matrices_from_file(file_path_full_board)  # plansza z już ułożonymi elementami

    # wczytanie elementów już wstawionych na planszę
    number_matrices = load_matrices_from_file(file_path_board_to_solve)  # plansza z częsciowo ułożonymi elementami
    number_matrices.pop(0)

    # transformacja elemntów obu macierzy
    for number, matrix in full_number_matrices.items():
        full_number_matrices[number] = shorten_matrix(matrix)

    for number, matrix in number_matrices.items():
        number_matrices[number] = shorten_matrix(matrix)

    # wyfiltrowanie elementów, które trzeba wstawić na planszę częściowo ułożoną
    number_matrices = {key: value for key, value in full_number_matrices.items() if key not in number_matrices}

    return number_matrices