import numpy as np

def input_Matrix(prompt):
    print(prompt)
    rows = int(input("Enter the number of rows : "))
    cols = int(input("Enter the number of columns : "))

    matrix = []

    for i in range(rows):
        row = list(map(float,input(f"Row {i+1}:").split()))
        if(len(row)!=cols):
            print("Number of rows must match the number of columns.")
            return None
        matrix.append(row)
    return np.array(matrix)

def operations():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Exit")

        choice = input("Enter your choice here : ")

        if choice=="4":
            break

        mat1 = input_Matrix("Enter the first matrix here : ")
        mat2 = input_Matrix("Enter the second matrix here : ")

        if choice == "1":
            if mat1.shape == mat2.shape:
                print("Result : \n", mat1+mat2)
            else:
                print("Matrix must be of the same order for addition.")
        elif choice == "2":
            if mat1.shape == mat2.shape:
                print("Result : \n", mat1-mat2)
            else:
                print("Matrix must be of the same order for subtraction.")
        elif choice == "3":
            if mat1.shape[1] == mat2.shape[0]:
                print("Result :  \n",np.dot(mat1,mat2))
            else:
                print("The no of columns in matrix 1 should be equal to no of rows in matrix 2")
        else :
            print("Invalid Input Choice")

if __name__ == '__main__':
    operations()