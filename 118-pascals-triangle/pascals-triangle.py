class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row=[]
        for i in range(numRows):
            row1=[1]*(i+1)
            for j in range(1,i):
                row1[j]=row[i-1][j-1]+row[i-1][j]
            row.append(row1)
        return row
