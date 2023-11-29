class Field:

    def __init__(self, mines=15, rows=10, columns=10):
        self.num_of_mines = mines
        self.num_of_rows = rows
        self.num_of_column = columns
        self.matrix = self.make_numbers()

    def create_field(self):
        import random
        nums = [i for i in range(self.num_of_rows*self.num_of_column)]
        random.shuffle(nums)
        array_field = [' ' for _ in range(self.num_of_rows*self.num_of_column)]
        for num in nums[:self.num_of_mines]:
            array_field[num] = '*'
        field = [array_field[i:i+self.num_of_column] for i in range(0, len(array_field), self.num_of_column)]
        return field

    def make_numbers(self):
        matrix = self.create_field()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                k = 0
                if i != 0 and j != 0:
                    if matrix[i-1][j-1] == '*':
                        k += 1  # left-up
                if j != 0:
                    if matrix[i][j-1] == '*':
                        k += 1  # left
                if i != len(matrix)-1 and j != 0:
                    if matrix[i+1][j-1] == '*':
                        k += 1  # left-down
                if i != len(matrix)-1:
                    if matrix[i+1][j] == '*':
                        k += 1  # down
                if i != len(matrix)-1 and j != len(matrix[i])-1:
                    if matrix[i+1][j+1] == '*':
                        k += 1  # right-down
                if j != len(matrix[i])-1:
                    if matrix[i][j+1] == '*':
                        k += 1  # right
                if i != 0 and j != len(matrix[i])-1:
                    if matrix[i-1][j+1] == '*':
                        k += 1  # right-up
                if i != 0:
                    if matrix[i-1][j] == '*':
                        k += 1  # up
                if k != 0 and matrix[i][j] != '*':
                    matrix[i][j] = k
        return matrix

    def print_of_field(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(self.matrix[i][j], end=' ')
            print()
