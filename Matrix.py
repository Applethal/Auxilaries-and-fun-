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

    def display_row(self):
        k = int(input("Choose which row to in the matrix that you wish to display"))
        k -= 1
        row = self.matrix[k]
        print(row)
    def display_column(self):
        m = int(input("Choose which column you wish to display in your matrix"))
        column = []
        m -= 1
        for  i in range(len(self.matrix)):
            number = self.matrix[i][m]
            column.append(number)
        print(column)
    
    # supose I want to multiply the same matrix by itself just for the sake of exercising
    
    def multiplication(self):
        matrix_m = []
        for j in range(len(self.matrix[0])):
            columns = []
            for i in range(len(self.matrix)):
                number = self.matrix[i][j]
                columns.append(number)
    
            rowss = []
            for i in range(len(self.matrix)):
                new_number = 0
                for k in range(len(self.matrix[0])):
                    new_number += self.matrix[i][k] * columns[k]
                rowss.append(new_number)
            matrix_m.append(rowss)
        for l in matrix_m:
            print(l)


       
            
        
        
            
    
    
    
        

    def print_matrix(self):
        for row in self.matrix:
            print(row)


def main():
    matrix_instance = matrix()
    matrix_instance.create_matrix()
    matrix_instance.print_matrix()
    matrix_instance.display_row()
    matrix_instance.display_column()
    matrix_instance.multiplication()


if __name__ == '__main__':
    main()
