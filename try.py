import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np

class MatrixCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")
        
        self.operation_var = tk.StringVar()
        self.matrix1_var = tk.StringVar()
        self.matrix2_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for Matrix 1
        ttk.Label(self.root, text="Matrix 1:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.matrix1_var, width=50).grid(row=0, column=1, padx=5, pady=5)

        # Label and Entry for Matrix 2
        ttk.Label(self.root, text="Matrix 2:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.matrix2_var, width=50).grid(row=1, column=1, padx=5, pady=5)

        # Operation Dropdown
        ttk.Label(self.root, text="Operation:").grid(row=2, column=0, padx=5, pady=5)
        operation_options = ["Addition", "Subtraction", "Multiplication", "Division", "Transpose", "Inverse", "Determinant"]
        ttk.Combobox(self.root, textvariable=self.operation_var, values=operation_options, state="readonly").grid(row=2, column=1, padx=5, pady=5)

        # Calculate Button
        ttk.Button(self.root, text="Calculate", command=self.calculate).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Result Textbox
        self.result_textbox = tk.Text(self.root, height=10, width=50)
        self.result_textbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def calculate(self):
        try:
            matrix1 = np.array(eval(self.matrix1_var.get()))
            matrix2 = np.array(eval(self.matrix2_var.get()))

            op_index = ["Addition", "Subtraction", "Multiplication", "Division", "Transpose", "Inverse", "Determinant"].index(self.operation_var.get()) + 1

            if 1 <= op_index <= 4:
                if matrix1.shape != matrix2.shape:
                    raise ValueError("Matrices must have the same shape for addition, subtraction, and division.")

            if op_index == 5:
                matrix = matrix1
            elif op_index in [1, 2, 3, 4]:
                matrix = (matrix1, matrix2)
            else:
                matrix = matrix1

            op = MatrixOperator(*matrix)
            result = None
            if op_index == 1:
                result = op.addition()
            elif op_index == 2:
                result = op.subraction()
            elif op_index == 3:
                result = op.multiply()
            elif op_index == 4:
                result = op.division()
            elif op_index == 5:
                result = op.transpose()
            elif op_index == 6:
                result = op.inverse()
            elif op_index == 7:
                result = op.determinant()

            if result is not None:
                self.result_textbox.delete('1.0', tk.END)
                self.result_textbox.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
app = MatrixCalculator(root)
root.mainloop()
