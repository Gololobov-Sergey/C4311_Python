import tkinter as tk

def click():
    label.config(text="Hello " + text.get())


window = tk.Tk()
window.geometry("600x400+600+200")
window.title("C4311")
# window.minsize(400, 400)
window.resizable(False, False)

label = tk.Label(text="Hello Python", font=("Comic Sans MS", 20, 'bold'), fg='crimson', bg='yellow', padx=30, pady=30)
label.pack()


text = tk.Entry()
text.pack()

button = tk.Button(text="Click My", command=click)
button.pack()





window.mainloop()