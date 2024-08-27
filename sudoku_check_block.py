def block_ok(sudoku,row_index,column_index):
    block_ok = True
    grid = []
    accepting_index = [0,3,6]
    if row_index not in accepting_index or column_index not in accepting_index:
        block_ok = False
    else:     
        for i in range(3):
            for y in range(3):
                current_value = sudoku[row_index+y][column_index+i]
                if current_value > 0: 
                    grid.append(current_value)
    
        
        for x in range(1,10):
            item_to_count = x
            count = 0
            for value in grid:
                if value == item_to_count:
                    count += 1
                    if count > 1: 
                        block_ok = False
                        break

    print(grid)
    return block_ok

def main():     
    sudoku = [         
        [9, 0, 0, 0, 8, 0, 3, 0, 0],         
        [2, 0, 0, 2, 5, 0, 7, 0, 0],         
        [0, 2, 0, 3, 0, 0, 0, 0, 4],         
        [2, 9, 4, 0, 0, 0, 0, 0, 0],         
        [0, 0, 0, 7, 3, 0, 5, 6, 0],         
        [7, 0, 5, 0, 6, 0, 4, 0, 6],         
        [0, 0, 7, 8, 0, 3, 9, 0, 0],         
        [0, 0, 1, 0, 0, 0, 0, 0, 3],         
        [3, 0, 0, 0, 0, 0, 0, 0, 2]     
        ]      
    print(block_ok(sudoku, row_index=0, column_index=0))    # False 
    print(block_ok(sudoku, row_index=3, column_index=6))    # False 
    print(block_ok(sudoku, row_index=6, column_index=3))    # True 

if __name__ == "__main__":     
    main() 