from copy import deepcopy

def new_doubled_matrix(matrix):
    new_matrix = deepcopy(matrix)
    for row in range(len(new_matrix)):
        for x in range(len(new_matrix[row])):
            new_matrix[row][x] = matrix[row][x]*2
    return new_matrix

def main(): 
    m1 = [[1, 2, 3], [4, 5, 6]] 
    m2 = new_doubled_matrix(m1) 
    print(m1) 
    print(m2) 

main() 