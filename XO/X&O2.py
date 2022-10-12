from tkinter import *
import random
root = Tk()
root.title('Х&О')
game_run = True
field = []
Fmas =[]
cross_count = 0

#обработчик нажатия кнопок

def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0

def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        if game_run and cross_count % 2 == 0:
            field[row][col]['text'] = 'X'
            global cross_count
            cross_count += 1
            check_win('X')
        elif game_run and cross_count % 2 == 1:       
            field[row][col]['text'] = 'O'
            cross_count += 1
        check_win('O')    


        
       
#def Click(row, col): 
 #   if game_run and field[row][col]['text'] == ' ':
  #      field[row][col]['text'] = 'O'
   #     global cross_count
    #    cross_count += 1
     #   check_win('O')
        
        

def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False         

for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='Новая игра', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()    
 
