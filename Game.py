import tkinter as tk
from pygame import mixer

time = 100
score = 0
press_enter = True

window = tk.Tk()
window.geometry("600x600+600+100")
window.resizable(False, False)
window.title("C4311 - Clicker")
window.iconbitmap("Pics/bomb.ico")

label = tk.Label(text="Для початку гри нажміть [ENTER]", font=('Comic Sans MS', 12, 'bold'))
label.pack()

label_time = tk.Label(text=f"Залишок часу {time}", font=('Comic Sans MS', 16, 'bold'))
label_time.pack()

label_score = tk.Label(text=f"Набрані бали {score}", font=('Comic Sans MS', 16, 'bold'))
label_score.pack()


img1 = tk.PhotoImage(file='Pics/1.gif')
img2 = tk.PhotoImage(file='Pics/2.gif')
img3 = tk.PhotoImage(file='Pics/3.gif')
img4 = tk.PhotoImage(file='Pics/4.gif')

label_bomb = tk.Label(image=img1)
label_bomb.pack()

def is_alive():
    global time
    if time <= 0:
        time = 0
        label.config(text="Бабах!", fg="red")
        mixer.init()
        mixer.music.load('b.mp3')
        mixer.music.play()
        return False
    else:
        return True

def update_screen():
    if time >= 80:
        label_bomb.config(image=img1)
    elif 80 > time >= 50:
        label_bomb.config(image=img2)
    elif 0 < time < 50:
        label_bomb.config(image=img3)
    else:
        label_bomb.config(image=img4)

    label_time.config(text=f"Залишок часу {time}")
    label_score.config(text=f"Набрані бали {score}")
    label_bomb.after(100, update_screen)

def update_time():
    global time
    time -= 5
    if is_alive():
        label_time.after(500, update_time)


def update_score():
    global score
    score += 1
    if is_alive():
        label_score.after(1000, update_score)


def start(event):
    global press_enter
    if not press_enter:
        pass
    else:
        press_enter = False
        label.config(text="")
        update_score()
        update_time()
        update_screen()

def click():
    global time
    if is_alive() and press_enter == False:
        time += 1

click = tk.Button(text="Тикай сюди", font=('Comic Sans MS', 16, 'bold'), fg="white", bg="black", command=click)
click.pack()

window.bind('<Return>', start)

window.mainloop()