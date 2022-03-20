
def find_element(matrix,i,j,target)->bool:
    if i<=j:
        mid=i+((j-i)//2)
        col=len(matrix[0])
        mid_matrix=matrix[mid//col][mid%col]
    
        if target==mid_matrix:
            return True
        
        else:
            if target<mid_matrix:
                j=mid-1
                return(find_element(matrix,i,j,target))
            else:
                i=mid+1
                return(find_element(matrix,i,j,target))
            
           
    else:
        return False
    

matrix=[[1,3,5,7],[10,11,15,17],[22,29,32,45]]
target=int(input("Enter value to be searched: "))
m=len(matrix)
n=len(matrix[0])
j=m*n-1
result=find_element(matrix,0,j,target)
print(result)
