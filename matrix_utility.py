import numpy as np

# funkcja usuwa zbędną pustą przestrzeń (pusta przestrzeń reprezentowana jest przez 0)
# przykładowo dla macierzy:
# 0 0 0 0
# 0 1 1 0
# 0 1 0 0
# 0 0 0 0
# funkcja zwraca nową macierz postaci:
# 1 1
# 1 0
def shorten_matrix(input_matrix):
    # znalezienie minimalnych wymiarów
    min_row, max_row, min_col, max_col = float('inf'), 0, float('inf'), 0
    for row_index, row in enumerate(input_matrix):
        for col_index, value in enumerate(row):
            if value != 0:
                min_row = min(min_row, row_index)
                max_row = max(max_row, row_index)
                min_col = min(min_col, col_index)
                max_col = max(max_col, col_index)

    # transformacja macierzy do nowej postaci
    transformed_matrix = [
        row[min_col:max_col + 1] for row in input_matrix[min_row:max_row + 1]
    ]

    return transformed_matrix

# sprawdcza, czy możliwe jest wtawienie wszystkich elementów macierzy do większej macierzy
# jeżeli element w większej macierzy to 0, a w mniejszej macierzy jest liczba różna od zera - można dodać
# jeżeli element w większej macierzy to nie 0 (czyli już wstawiony, inny element),
# a w mniejszej macierzy jest liczba różna od zera - nie można wstawić tego elementu w tym indeksie
# zwraca flagę, która mówi, czy możliwe jest dodanie
def can_place_matrix(larger_matrix, smaller_matrix, row, col):
    larger_rows = len(larger_matrix)
    larger_cols = len(larger_matrix[0])
    smaller_rows = len(smaller_matrix)
    smaller_cols = len(smaller_matrix[0])

    # sprawdzenie, czy wymiary się zgadzają
    if row + smaller_rows > larger_rows or col + smaller_cols > larger_cols:
        return False

    # sprawdzczenie, czy możliwe jest wstawienie,
    # zaczynamy od lewego górnego rogu małej macierzy
    for i in range(smaller_rows):
        for j in range(smaller_cols):
            if smaller_matrix[i][j] != 0 and larger_matrix[row + i][col + j] != 0:
                return False

    return True


# jeśli to możliwe, to umieszcza mniejszą macierz reprezentującą element,
# do macierzy większej reprezentującej ułożoną planszę
# zwraca flagę informującą, czy dodanie się powiodło
def insert_matrix(larger_matrix, smaller_matrix, row, col):
    if can_place_matrix(larger_matrix, smaller_matrix, row, col):
        for i in range(len(smaller_matrix)):
            for j in range(len(smaller_matrix[0])):
                if (smaller_matrix[i][j] != 0):
                    larger_matrix[row + i][col + j] = smaller_matrix[i][j]
        return True
    else:
        return False


# funckja zwraca wszystkie możliwe kombinacje ułożenia elementu
# element możemy obracać i odbijać, więc wszystkich kombinacji jest 8
# wykorzstuje biblioteke z zakresu algebry liniowej do obrotu macierzy
def generate_rotations_and_flips(matrix):
    combinations = []
    original_matrix = np.array(matrix)

    for flip in [False, True]:
        for rotate_angle in [0, 90, 180, 270]:
            rotated_matrix = np.rot90(original_matrix, rotate_angle // 90)
            if flip:
                rotated_matrix = np.flip(rotated_matrix, axis=1)

            combinations.append(rotated_matrix.tolist())

    return combinations

