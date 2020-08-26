# Clicker Game
import tkinter as tk
import os, sys

game_window = tk.Tk(); game_window.title('gamer')

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

def destroy():
    game_window.destroy()

frame_1 = tk.Frame(master = game_window,
                   ); frame_1.pack(fill = tk.BOTH)

label_1 = tk.Label(master = frame_1,
                   text = 'You need more to conquer this galaxy...',
                   relief = tk.SOLID,
                   borderwidth = 2,
                   font = 'consolas',
                   ); label_1.grid(row = 0, column = 0, columnspan = 3)

game_num = tk.Label(master = frame_1,
                    text = 'Soldiers\n0',
                    font = 'consolas',
                    ); game_num.grid(row = 1, column = 1, padx = 2)

frame_2 = tk.Frame(master = game_window,
                   );frame_2.pack(side = 'bottom', fill = tk.BOTH)

spacer1 = tk.Label(master = frame_2,
                   width = 4,
                   height = 2,
                   text = '   '); spacer1.grid(row = 0, column = 0)

clicker = tk.Button(master = frame_2,
                    text = 'Train more',
                    font = 'consolas',
                    borderwidth = 5,
                    ); clicker.grid(row = 0, column = 2, padx = 2)

escape = tk.Button(master = frame_2,
                   text = 'exit',
                   command = destroy,
                   font = 'consolas',
                   borderwidth = 5,
                   ); escape.grid(row = 1, column = 2, padx = 2)

settings = tk.Button(master = frame_2,
                     text = 'settings',
                     font = 'consolas',
                     borderwidth = 5,
                     ); settings.grid(row = 0, column = 1)

upgrades = tk.Button(master = frame_2,
                     text = 'upgrades',
                     font = 'consolas',
                     borderwidth = 5,
                     ); upgrades.grid(row = 0, column = 3)


clicker.bind('<ButtonRelease-1>', button_press)

        




while True:
    game_num.config(text = f'Soldiers\n{get_num()}')
    game_window.update()
    game_window.update_idletasks()
