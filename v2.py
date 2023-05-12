import tkinter as tk
from tkinter import Label, StringVar, Entry, Frame, Button

#Sudoku Solver -----------------------------------------
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
        elif grid[x][col] == num:
            return False

    startRow, startCol = row - row % 3, col - col % 3
    for y in range(3):
        for x in range(3):
            if grid[y + startRow][x + startCol] == num:
                return False
    return True
 
def sudoku(grid, row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return sudoku(grid, row, col + 1)

    for num in range(1, 10): 
        if solve(grid, row, col, num):
            grid[row][col] = num
            if sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

#GUI ---------------------------------------------------
bgcolor = '#25b8ea'
app = tk.Tk()
app.config(bg=bgcolor)
app.geometry('900x700')
app.title(f'Sudoku Solver v1.1')
app.resizable(False, False)

canvas = tk.Canvas(app, width=900, height=700, bg=bgcolor)
canvas.place(x=0, y=0)

titlelbl = tk.Label(app, text = f'Sudoku Solver v1.1', bg=bgcolor, font='Arial 35 bold', fg='white').place(x=100, y=20)

rows, columns, cellwidth, cellheight = 9, 9, 50, 50
cells, inputs = {}, []

def button_clear():
    for x in inputs:
        for _, r in enumerate(x.get()):
            x.delete(0)
        
def button_solve():
    grid = [[0] * 9 for _ in range(9)]
    for i, x in enumerate(inputs):
        t = x.get()
        if len(t) > 1:
            print("Number should only be 1 digit.")
            return
        if t:
            try:
                grid[i // 9][i % 9] = int(t)
            except:
                print("Please only use numbers.")
                return
    
    if sudoku(grid, 0, 0):
        button_clear()
        puzzle_placement = 0
        for y in range(9):
            for x in range(9):
                inputs[puzzle_placement].insert('end',grid[y][x])
                puzzle_placement += 1
    else:
        print("Solution does not exist.")

#Build Grid
for row in range(1, 10):
    for col in range(1, 10):
        input_cell = StringVar()
        input_box = Entry(app, textvariable=input_cell, font='Arial 20', width=2, justify='center')
        input_box.place(x=row*cellwidth+350, y=col*cellheight+100)
        inputs.append(input_box)

solvebtntext, clearbtntext = StringVar(), StringVar()

solvebtn = tk.Button(app, textvariable=solvebtntext, font='Arial 15 bold', bd=0, bg='white', command=button_solve)
solvebtntext.set("Solve")
solvebtn.place(x=100, y=493)

clearbtn = tk.Button(app, textvariable=clearbtntext, font='Arial 15 bold', bd=0, bg='white', command=button_clear)
clearbtntext.set("Clear Board")
clearbtn.place(x=100, y=553)

app.mainloop()
