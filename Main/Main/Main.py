# Clicker Game
import tkinter as tk
import os, sys

game_window = tk.Tk(); game_window.title('gamer')

# opens the save file and gets the number, if it doesn't exist then it creates the file and puts its value to zero
def get_num():
    try:
        with open(os.path.join(sys.path[0])+'/saves/save.txt', 'r') as file:
            return(str(file.read()))
    except:
        with open(os.path.join(sys.path[0])+'/saves/save.txt', 'w+') as file:
            file.write('0')
            return(str(file.read()))

# Adds one soldier to the count
def button_press(event):
    with open(os.path.join(sys.path[0])+'/saves/save.txt', 'r+') as file:
        num1 = int(file.read())
        num1 += 1
        file.seek( 0, 0 )
        file.write(str(num1))

# cloes the game window
def destroy():
    game_window.destroy()

# Settings GUi / code
def settings():
    
    # this function will be called by the "reset" button
    def settings_reset_game():

        
        def reset():
            with open(os.path.join(sys.path[0])+'/saves/save.txt', 'w+') as file:
                file.write('0')
            kill_window.destroy()


        def kill_window_deny():
            kill_window.destroy()
    
        kill_window = tk.Tk(); kill_window.title('are you sure?')
        f1 = tk.Frame(kill_window); f1.pack(fill = tk.BOTH)
        l1 = tk.Label(f1, text='Are you sure you want to reset?', font = 'consolas'); l1.grid(row = 0, column = 0)
        f2 = tk.Frame(kill_window); f2.pack(fill = tk.BOTH, side = 'bottom')
        spacer_kwindow = tk.Label(f2, text = '', width = 13); spacer_kwindow.grid(row = 0, column = 0)
        b1 = tk.Button(f2, text = 'yes', font = 'consolas', command = reset, borderwidth = 5);b1.grid(row = 0, column = 1)
        b2 = tk.Button(f2, text = 'no', font = 'consolas', command = kill_window_deny, borderwidth = 5);b2.grid(row = 0, column = 2)

    def escape_settings():
        setting_window.destroy()

    setting_window = tk.Tk(); setting_window.title('Settings')

    s_frame = tk.Frame(setting_window);s_frame.pack()

    b_reset = tk.Button(s_frame, text = 'Reset', font = 'consolas', borderwidth = 5, command = settings_reset_game); b_reset.grid(row = 0, column = 0)

    b_escape = tk.Button(s_frame, text = 'Escape', font = 'consolas', borderwidth = 5, command = escape_settings); b_escape.grid(row = 1, column = 0)




# Main Game window GUI
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
                     command = settings,
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