def print_matrix_sum(m1,m2):
    for i in range(len(m1)):
        for x in range (len(m1[0])):
            print(m1[i][x] + m2[i][x],end =" ")
        print()
    
 

def main(): 
    m1 = [[1, 2, 0], [2, 3, 4]] 
    m2 = [[3, 2, 5], [6, 4, 3]] 
    m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]] 
    m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]] 
    
    print_matrix_sum(m1, m2) 
    print() 
    print_matrix_sum(m3, m4)

if __name__ == "__main__":
    main()