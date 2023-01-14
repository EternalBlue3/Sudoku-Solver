import tkinter as tk
from tkinter import Label, StringVar, Entry, Frame, Button

#Sudoku Solver -----------------------------------------
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
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
version = 1.0
app = tk.Tk()
app.config(bg=bgcolor)
app.geometry('900x700')
app.title(f'Sudoku Solver v{version}')
app.resizable(False, False)

canvas = tk.Canvas(app, width=900, height=700, bg=bgcolor)
canvas.place(x=0, y=0)

titlelbl = tk.Label(app, text = f'Sudoku Solver v{version}', bg=bgcolor, font='Arial 35 bold', fg='white').grid(row=0, column=0, columnspan=10)

rows = 9
columns = 9
cellwidth = 50
cellheight = 50

cells = {}
inputs = []

def button_clear():
    for x in inputs:
        r = len(x.get())
        for t in range(r):
            x.delete(r - (t+1))
        
def button_solve():
    grid = [[0] * 9 for _ in range(9)]
    for i, x in enumerate(inputs):
        t = x.get()
        if t:
            grid[i // 9][i % 9] = int(t)
    if sudoku(grid, 0, 0):
        button_clear()
        puzzle_placement = 0
        for v in range(9):
            for c in range(9):
                inputs[puzzle_placement].insert('end',grid[v][c])
                puzzle_placement += 1
    else:
        print("Solution does not exist")

#Build Grid
for row in range(1,10):
    for column in range(1,10):
        selected = False
        
        if row in [4,5,6] and column in [4,5,6]:
            cell = Frame(app, bg='black', highlightbackground="black", highlightcolor="black", highlightthickness=2, width=50, height=50,  padx=3,  pady=3, background='black')
            selected = True
                
        if row in [1,2,3,7,8,9] and column in [1,2,3]:
            cell = Frame(app, bg='black', highlightbackground="black", highlightcolor="black", highlightthickness=2, width=50, height=50,  padx=3,  pady=3, background='black')
            selected = True
                
        if row in [1,2,3,7,8,9] and column in [7,8,9]:
            cell = Frame(app, bg='black', highlightbackground="black", highlightcolor="black", highlightthickness=2, width=50, height=50,  padx=3,  pady=3, background='black')
            selected = True
                
        if selected == False:
            cell = Frame(app, bg='black', highlightbackground="blue", highlightcolor="blue", highlightthickness=2, width=50, height=50,  padx=3,  pady=3, background='black')
            
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell
        v = Entry(cells[row,column], width=3)
        v.pack()
        inputs.append(v)

solvebtntext, clearbtntext = StringVar(), StringVar()

solvebtn = tk.Button(app, textvariable=solvebtntext, font='Arial 15 bold', bd=0, bg='white', command=button_solve)
solvebtntext.set("Solve")
solvebtn.grid(padx=30,pady=0)

clearbtn = tk.Button(app, textvariable=clearbtntext, font='Arial 15 bold', bd=0, bg='white', command=button_clear)
clearbtntext.set("Clear Board")
clearbtn.grid(padx=30,pady=30)

app.mainloop()
