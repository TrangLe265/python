def column_ok(sudoku, column_index):
    column_ok = True

    for i in range(1,10):
        item_to_count = i
        count = 0
        for row in sudoku:
            if row[column_index] == item_to_count:
                count += 1
                if count > 1: 
                    column_ok = False
                    break
    return column_ok

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
    
    print(column_ok(sudoku, column_index=0))    # False      
    print(column_ok(sudoku, column_index=1))    # True     
    print(column_ok(sudoku, column_index=8))    # 

if __name__ == "__main__":     
    main()  