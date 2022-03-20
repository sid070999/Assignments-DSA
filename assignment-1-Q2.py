

def find_element2D(matrix,no_rows,no_col,target):
    rows=no_rows-1
    cols=0
    while rows>=0 and cols<no_col:
        if matrix[rows][cols]==target:
            return True
        elif matrix[rows][cols]>target:
            rows-=1
        else:
            cols+=1
    return False


matrix=[[1,4,7,11,15], [2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,28,30]]
target=int(input("Enter value to be searched: "))
no_rows=len(matrix)
no_col=len(matrix[0])
K=find_element2D(matrix,no_rows,no_col,target)
print(K)