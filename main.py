import tkinter
from tkinter import Label, StringVar, Entry, Frame, Button
from tkinter.constants import DISABLED, NORMAL

#Sudoku Solver -----------------------------------------
M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
        
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
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

#GUI ---------------------------------------------------
bgcolor = '#25b8ea'
version = 1.0
app = tkinter.Tk()
app.config(bg=bgcolor)
app.geometry('700x700')
app.title(f'Sudoku Solver v{version}')
app.resizable(False, False)

canvas = tkinter.Canvas(app, width=700, height=700, bg=bgcolor)
canvas.place(x=0, y=0)

titlelbl = tkinter.Label(app, text = f'Sudoku Solver v{version}', bg=bgcolor, font='Arial 35 bold', fg='white').grid(row=0, column=0, columnspan=10)

rows = 9
columns = 9
cellwidth = 50
cellheight = 50

cells = {}
inputs = []

def buttonclear():
    for x in inputs:
        r = len(x.get())
        for t in range(r):
            x.delete(r - (t+1))

#btnsolve
def buttonsolve():
    '''0 means the cells where no value is assigned'''
    grid = []
    grid1 = []
    grid2 = []
    grid3 = []
    grid4 = []
    grid5 = []
    grid6 = []
    grid7 = []
    grid8 = []
    grid9 = []
    
    tally = 8
    for x in inputs:
        tally += 1
        t = x.get()
        if t == '':
            gridder = f"grid{str(tally//9)}.append(0)"
            exec(gridder)
        else:
            gridder = f"grid{str(tally//9)}.append(int(t))"
            exec(gridder)
            
    for l in range(1,10):
        grid_appender = f"grid.append(grid{l})"
        exec(grid_appender)
            
    if (Suduko(grid, 0, 0)):
        buttonclear()
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
        
        if row == 4 or row == 5 or row == 6:
            if column == 4 or column == 5 or column == 6:
                cell = Frame(app, bg='black', highlightbackground="black", highlightcolor="black", highlightthickness=2, width=50, height=50,  padx=3,  pady=3, background='black')
                selected = True
                
        if row == 1 or row == 2 or row == 3 or row == 7 or row == 8 or row == 9:
            if column == 1 or column == 2 or column == 3:
                cell = Frame(app, bg='black', highlightbackground="black", highlightcolor="black", highlightthickness=2, width=50, height=50,  padx=3,  pady=3, background='black')
                selected = True
                
        if row == 1 or row == 2 or row == 3 or row == 7 or row == 8 or row == 9:
            if column == 7 or column == 8 or column == 9:
                cell = Frame(app, bg='black', highlightbackground="black", highlightcolor="black", highlightthickness=2, width=50, height=50,  padx=3,  pady=3, background='black')
                selected = True
                
        if selected == False:
            cell = Frame(app, bg='black', highlightbackground="blue", highlightcolor="blue", highlightthickness=2, width=50, height=50,  padx=3,  pady=3, background='black')
            
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell
        v = Entry(cells[row,column], width=3)
        v.pack()
        inputs.append(v)
        
solvebtntext = StringVar()
clearbtntext = StringVar()

solvebtn = tkinter.Button(app, textvariable=solvebtntext, font='Arial 15 bold', bd=0, bg='white', command=buttonsolve)
solvebtntext.set("Solve")
solvebtn.grid(padx=30,pady=0)

clearbtn = tkinter.Button(app, textvariable=clearbtntext, font='Arial 15 bold', bd=0, bg='white', command=buttonclear)
clearbtntext.set("Clear Board")
clearbtn.grid(padx=30,pady=30)

app.mainloop()
