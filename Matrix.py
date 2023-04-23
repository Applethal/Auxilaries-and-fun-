class matrix:
    def __init__(self):
        self.matrix = []

    def add_row(self):
        rows = int(input("Input the number of rows in the matrix"))
        return rows

    def add_column(self):
        columns = int(input("Input the number of columns that you wish to have in the matrix"))
        return columns

    def create_matrix(self):
        rows = self.add_row()
        columns = self.add_column()
        counter_r = 0
        counter_c = 0
        for row in range(rows):
            row = []
            self.matrix.append(row)
            counter_r += 1
            for column in range(columns):
                if counter_c == columns:
                    counter_c = 0
                counter_c += 1
                number = int(input(f"Input the number in row {counter_r}, column  {counter_c}:"))
                row.append(number)

    def multiplication(self):
        self.add_row()
        self.add_column()
        if len(self.matrix[1]) != self.add_column:
            print(
                "Sorry, I don't think that's how multiplying a matrix works, the lenght of the row should match the lenght of the column of the array that you wish to multiply the matrix with."
            )
        else 
            m_rows = self.add_row()
            m_columns = self.add_column()
            m_matrix = []
            m_counter_c = 0
            m_counter_r = 0
            for i in range(m_rows):
                i = []
                m_matrix.append(i)
                m_counter_r += 1
                for j in range(m_columns):
                    if m_counter_c == m_columns:
                        m_counter_c = 0
                    m_counter_c += 1
                    n = int(input(f"Input the number in row {m_counter_r}, column  {m_counter_c}:"))
                    i.append(n)
            for i in self.matrix:
                for j in self.matrix[i]:
                    self.matrix[i][j] = self.matrix[j] * m_matrix[i][j]

    def print_matrix(self):
        for row in self.matrix:
            print(row)


def main():
    matrix_instance = matrix()
    matrix_instance.create_matrix()
    matrix_instance.print_matrix()
    matrix_instance.multiplication()


if __name__ == '__main__':
    main()
