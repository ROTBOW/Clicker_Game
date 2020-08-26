# Clicker Game
import tkinter as tk
import os, sys

game_window = tk.Tk(); game_window.title('gamer')

frame_1 = tk.Frame(master = game_window,
                   ); frame_1.pack(fill = tk.BOTH)

label_1 = tk.Label(master = frame_1,
                   text = 'You need more to conquer this galaxy...',
                   relief = tk.SOLID,
                   borderwidth = 2,
                   font = 'consolas',
                   ); label_1.grid(row = 0, column = 1, pady = 5)

game_num = tk.Label(master = frame_1,
                    text = 'Soldiers\n0',
                    font = 'consolas',
                    ); game_num.grid(row = 1, column = 1, padx = 2, pady = 2)

clicker = tk.Button(master = frame_1,
                    text = 'Train more',
                    font = 'consolas',
                    borderwidth = 5,
                    ); clicker.grid(row = 2, column = 1, padx = 2, pady = 2)

def get_num():
    try:
        with open(os.path.join(sys.path[0])+'/saves/save.txt', 'r') as file:
            return(str(file.read()))
    except:
        with open(os.path.join(sys.path[0])+'/saves/save.txt', 'w+') as file:
            file.write('0')
            return(str(file.read()))

def button_press(event):
    with open(os.path.join(sys.path[0])+'/saves/save.txt', 'r+') as file:
        num1 = int(file.read())
        num1 += 1
        file.seek( 0, 0 )
        file.write(str(num1))

clicker.bind('<ButtonRelease-1>', button_press)

        




while True:
    game_num.config(text = f'Soldiers\n{get_num()}')
    game_window.update()
    game_window.update_idletasks()
