def row_ok(sudoku, row_index):
    row = sudoku[row_index]
    row_ok = True
    
    
    for element in row:
        if element > 0: 
           count = row.count(element)
           if count > 1: 
               row_ok = False
    
    return row_ok


def main():     
    sudoku = [ 
        [9, 0, 0, 0, 8, 0, 3, 0, 0],       #0
        [2, 0, 0, 2, 5, 0, 7, 0, 0],       #1  
        [0, 2, 0, 3, 0, 0, 0, 0, 4],       #2
        [2, 9, 4, 0, 0, 0, 0, 0, 0],       #3  
        [0, 0, 0, 7, 3, 0, 5, 6, 0],       #4
        [7, 0, 5, 0, 6, 0, 4, 0, 0],       #5
        [0, 0, 7, 8, 0, 3, 9, 0, 0],       #6 
        [0, 0, 1, 0, 0, 0, 0, 0, 3],       #7 
        [3, 0, 0, 0, 0, 0, 0, 0, 2]        #8
        ] 
    print(row_ok(sudoku, row_index=0))        
    print(row_ok(sudoku, row_index=1))         
    print(row_ok(sudoku, row_index=8))
       
if __name__ == "__main__":     
    main() 