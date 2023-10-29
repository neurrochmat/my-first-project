def create_matrix(cols, rows):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            elem = int(input(f"Masukan angka untuk baris {i + 1}, kolom {j + 1}: "))
            row.append(elem)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)
        
if __name__ == "__main__":
    rows = int(input("Masukan jumlah baris: "))
    cols = int(input("Masukan jumlah kolom: "))
    
    matrix = create_matrix(rows, cols)
    print("Matrix yang dibuat: ")
    print_matrix(matrix)