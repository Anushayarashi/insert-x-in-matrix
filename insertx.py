row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]
posistion=[row1,row2,row3]
print(f"{row1}{row2}{row3}")
matrix=input("enter the posistion where you need to be insert")
row_num=int(matrix[0])
col_num=int(matrix[1])
final_matrix=posistion[row_num-1]
final_matrix[col_num-1]='*'
print(f"{row1}{row2}{row3}")