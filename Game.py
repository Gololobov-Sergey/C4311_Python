import tkinter as tk

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
    pass

def update_screen():
    pass

def update_time():
    pass


def update_score():
    pass


def start():
    pass

def click():
    pass

click = tk.Button(text="Тикай сюди", font=('Comic Sans MS', 16, 'bold'), fg="white", bg="black")
click.pack()

window.mainloop()