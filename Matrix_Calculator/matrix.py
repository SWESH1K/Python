
# Matrix Calculator --> made by Sweshik Reddy-2310080053.

import numpy as np

def printMatrix(matrix):
    print("="*41)
    for i in matrix:
        print('|',end=" ")
        for j in i:
            print(j,end="\t"+"|"+"\t")
        print()
        print('-'*41)
    print("="*41)

def takeInputTwo():
    try:
        # Take user input for the dimensions of the matrices
        rows1 = int(input("Enter the number of rows for matrix 1: "))
        cols1 = int(input("Enter the number of columns for matrix 1: "))

        rows2 = int(input("Enter the number of rows for matrix 2: "))
        cols2 = int(input("Enter the number of columns for matrix 2: "))

        if(cols1 != rows2): print(1/0)

        # Take user input for the elements of the matrices
        print("Enter the elements of matrix 1:")
        matrix1 = np.array([[int(input(f"Enter element for row {i+1} and column {j+1}: ")) 
                            for j in range(cols1)] for i in range(rows1)])

        print("\nEnter the elements of matrix 2:")
        matrix2 = np.array([[int(input(f"Enter element for row {i+1} and column {j+1}: ")) 
                        for j in range(cols2)] for i in range(rows2)])
    
        return matrix1,matrix2
    except:
        print("Please enter the valid inputs!")
        return takeInputTwo()

def takeInputOne():
    try:
        # Take user input for the dimensions of the matrix
        rows = int(input("Enter the number of rows for matrix: "))
        cols = int(input("Enter the number of columns for matrix: "))

        print("Enter the elements of matrix:")
        matrix = np.array([[int(input(f"Enter element for row {i+1} and column {j+1}: ")) 
                            for j in range(cols)] for i in range(rows)])
        
        return matrix
    except:
        print("Please enter the valid inputs!")
        return takeInputOne()

def getOperation():
    try:
        op = int(input("Please select the operation by entering the index: "))
        if op not in range(1,10):
            print("Please enter the valid index (Index not in range)")
            return getOperation()
        return op
    except:
        print("Please enter a number!")
        return getOperation()

class MatrixOperator:
    
    def __init__(self, matrix1,matrix2=None):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def addition(self):
        resultant = np.add(self.matrix1,self.matrix2)
        print("\nArray:1")
        printMatrix(self.matrix1)
        print("\nArray:2")
        printMatrix(self.matrix2)
        print("\nSUM:")
        printMatrix(resultant)
        return resultant

    def subraction(self):
        resultant = np.subtract(self.matrix1,self.matrix2)
        print("\nArray:1")
        printMatrix(self.matrix1)
        print("\nArray:2")
        printMatrix(self.matrix2)
        print("\nSUBRACTION:")
        printMatrix(resultant)
        return resultant    
    
    def multiply(self):
        resultant = np.dot(self.matrix1,self.matrix2)
        print("\nArray:1")
        printMatrix(self.matrix1)
        print("\nArray:2")
        printMatrix(self.matrix2)
        print("\nMULTIPLICATON:")
        printMatrix(resultant)
        return resultant
    
    def division(self):
        resultant = np.divide(self.matrix1,self.matrix2)
        print("\nArray:1")
        printMatrix(self.matrix1)
        print("\nArray:2")
        printMatrix(self.matrix2)
        print("\nDIVISION:")
        printMatrix(resultant)
        return resultant
    
    def transpose(self):
        resultant = np.transpose(self.matrix1)
        print("\nArray:")
        printMatrix(self.matrix1)
        print("\nTRANSPOSE:")
        printMatrix(resultant)
        return resultant
    
    def inverse(self):
        try:
            resultant = np.linalg.inv(self.matrix1)
            print("\nArray:1")
            printMatrix(self.matrix1)
            print("\nINVERSE:")
            printMatrix(resultant)
            return resultant
        except Exception as error:
            print("Matrix is singular and does not have an inverse.")
            print(error)

    def determinant(self):
        try:
            print("\nArray:1")
            printMatrix(self.matrix1)
            det = np.linalg.det(self.matrix1)
            det = format(det,".2f")
            print(f"Determinant of the matrix is: {det}")
            return det
        except np.linalg.LinAlgError:
            print("Matrix is singular and its determinant cannot be calculated.")

    def rank(self):
        rank = np.linalg.matrix_rank(self.matrix1)
        print("\nArray:1")
        printMatrix(self.matrix1)
        print("Rank=",rank)
        return rank
    
    def eigenValues(self):
        eigen = np.linalg.eigvals(self.matrix1)
        print("\nArray:1")
        printMatrix(self.matrix1)
        print("Eigen values = ",eigen)
        return eigen


def main():
    operations = ["Addition","Subraction","Multiplication","Division","Transpose","Inverse","Determinant","Rank","Eigen Values"]
    for i,op in enumerate(operations):
        print(f"{i+1},{op}",end=" | ")
    print()
    op = getOperation()
    if(op in range(1,5)):
        matrix1,matrix2 = takeInputTwo()
        resultant = MatrixOperator(matrix1,matrix2)
        match op:
            case 1:
                resultant.addition()
            case 2:
                resultant.subraction()
            case 3:
                resultant.multiply()
            case 4:
                resultant.division()
    else:
        matrix = takeInputOne()
        resultant = MatrixOperator(matrix)
        match op:
            case 5:
                resultant.transpose()
            case 6:
                resultant.inverse()
            case 7:
                resultant.determinant()
            case 8:
                resultant.rank()
            case 9:
                resultant.eigenValues()

if __name__=='__main__':
    main()