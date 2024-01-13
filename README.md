# Projekt "Układator puzzli" 

## Opis projektu
"Układator puzzli" jest prostą aplikacją stworzoną w języku Python. 
Aplikacja wizualizuje proces układa puzzli na danej przez użytkownika planszy, gdzie elementy puzzli 
mogą być zarówno obracane, jak i odwracane.

Algorytm wstawiania elementów na planszę jest wyjątkowo uproszczony i opiera się na losowym wyborze kolejnych elementów.
Głównym celem projektu była wizualizacja procesu układania, a nie przedstawienie najbardziej efektywnego algorytmu.

## Struktura projektu
Projekt składa się z kilku plików, każdy zawierający odpowiednie funkcję:

### W pliku **load_data.py**:

#### `parse_arguments()`
- funkcja odpowiedzialna za parsowanie argumentów wywołania programu przy użyciu modułu `argparse`
- zwraca krotkę z wczytanymi wartościami

#### `filter_out_elements_to_use(file_path_full_board, file_path_board_to_solve)`
- funkcja filtrująca elementy do ułożenia na podstawie już całkowicie ułożonej planszy
- zwraca słownik zawierający elementy, które jeszcze nie zostały umieszczone na planszy do ułożenia

### W pliku **solver.py**:

#### `put_any_piece_on_board(number_matrices, solved_matrix)`
- funkcja próbująca umieścić losowo obrócony element puzzla na planszy do ułożenia
- zwraca flagę informującą, czy udało się dodać element na planszę
- modyfikuje daną tablicę solved_matrix

### W pliku **renderer.py**:

#### `render_board(screen, solved_matrix)`
- funkcja odpowiedzialna za renderowanie planszy na ekranie i już umieszczonych na planszy elementów

#### `render_pieces(screen, number_matrices, board_offset_y)`
- funkcja rysująca pozostałe do ułożenia elementy pod planszą
- bierze pod uwagę wielkość okna do poprawnego wyświetlania elementów
- rysuje elementy pod planszą dzięki argumentowi board_offset_y

#### `render_background(screen)`
- funkcja ustawiająca tło ekranu

#### `render_success_message(screen, board_offset_y)`
- funkcja rysująca komunikat o ukończeniu układania puzzli na ekranie
- rysuje komunikat pod planszą dzięki argumentowi board_offset_y

#### `setup_window(width, height, rect_size)`
- funkcja inicjalizująca okno zdefiniowanych wymiarach
- zmienia wartość globalnego parametru rect_size

### W pliku **matrix_utility.py**:

#### `get_matrix_dimensions(file_path)`
- funkcja wczytująca wymiary macierzy z pliku

#### `read_matrix_from_file(file_path)`
- funkcja wczytująca macierz z pliku
- zwraca macierz, w której liczby całkowite reprezentują kolejne elementy

#### `load_matrices_from_file(file_path)`
- funkcja wczytująca macierze z pliku, używana do wczytania planszy z elementami ułożonymi
- zwraca słownik, gdzie klucze to liczby całkowite będące reprezentantami elementów, a za wartości posiada macierze zawierające strukturę elementu

#### `generate_rotations_and_flips(matrix)`
- funkcja generująca wszystkie możliwe kombinacje obrotów i odbić dla danej macierzy puzzla
- zwraca tablice, której elementy to macierze zawierające strukturę elementu

#### `can_place_matrix(larger_matrix, smaller_matrix, row, col)`
- funkcja sprawdzająca, czy możliwe jest umieszczenie elementów mniejszej macierzy do większej, startując od larger_matrx[row][col]
- jeżeli elementem na larger_matrx[row + i][col + j] jest 0 - możliwe jest wstawienie elementu smaller_matrix[row + i][col + j]
- jeżeli na pozyjach [row + i][col + j] obu macierzy jednocześnie jest coś innego niż 0 - niemożliwe jest wstawienie macierzy
- zwraca flagę informującą, czy możliwe jest dodanie

#### `insert_matrix(larger_matrix, smaller_matrix, row, col)`
- funkcja przenosząca elementy smaller_matrix do larger_matrix startując od pozycji [row][col]
- uprzednio sprawdza, czy wstawienie jest możliwe przy użyciu funkcji can_place_matrix
- zwraca flagę informującą, czy wstawiono macierz

#### `shorten_matrix(input_matrix)`
- funkcja usuwa zbędną pustą przestrzeń (pusta przestrzeń reprezentowana jest przez 0)
- przykładowo dla macierzy:
```0 0 0 0
0 1 1 0
0 1 0 0
0 0 0 0
```
funkcja zwraca nową macierz postaci:
```
1 1
1 0
```

### W pliku **main.py**:
- główny plik projektu, w którym znajduje się, pobranie danych wejściowych, inicjalizacja Pygame i uruchamianie algorytmu układającego puzzel


## Uruchomienie projektu
Aby uruchomić aplikację, należy użyć poniższego polecenia w terminalu:

```bash
python main.py -p plansza_ulozona.txt -n 1 -w 960 -h 600 -b 30 plansza_do_ulozenia.txt
```

Gdzie:
- `-p` to ścieżka do pliku z ułożoną planszą, domyślnie: "plansza.txt"
- `-n` to czas (w sekundach) między kolejnymi ruchami, domyślnie: 1
- `-w` szerokość okna w pikselach, domyślnie: 960
- `-h` wysokość okna w pikselach, domyślnie: 600
- `-b` długość boku kwadratu składającego się na element w pikselach, domyślnie: 30
- ostatni argument to ścieżka do pliku z planszą do ułożenia.

## Zależności
Projekt korzysta z biblioteki do wizualizacji - Pygame oraz biblioteki z zakresu algebry liniowej użytej do obrotów macierzy - numpy.
Do instalacji wymienionych bibliotek należy użyć polecenia:

```bash
pip install pygame
pip install numpy
```

## Autor
Autor:

---