import random
from matrix_utility import *

# funckja zwraca pomieszane wszystkie możliwe kombinacje - aby algorytm zachowywał się losowo
def get_all_possible_combinations(number_matrices):
    all_possible_combinations = {}
    keys_in_random_order = random.sample(list(number_matrices.keys()), len(number_matrices))

    for number in keys_in_random_order:
        matrix = number_matrices[number]
        random_rotations_and_flips = generate_rotations_and_flips(matrix)
        random.shuffle(random_rotations_and_flips)
        all_possible_combinations[number] = random_rotations_and_flips

    return all_possible_combinations


# jeżeli możliwe jest umieszczenie jakiegokolwiek elementu, to go umieszcza
# zwraca flagę, która informuje czy dodanie się powiodło
def put_any_piece_on_board(number_matrices, solved_matrix):
    all_possible_combinations = get_all_possible_combinations(number_matrices)
    height = len(solved_matrix)
    width = len(solved_matrix[0])

    for number, matrices in all_possible_combinations.items():
        for matrix in matrices:
            for row_to_insert in range(height):
                for col_to_insert in range(width):
                    added = insert_matrix(solved_matrix, matrix, row_to_insert, col_to_insert)
                    if added:
                        number_matrices.pop(number, None)
                        return True

    return False
