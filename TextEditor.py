import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def open_file(event=None):
    file_name = filedialog.askopenfilename(title="C4311 - Open file", defaultextension="txt", filetypes=(('Text files', '*.txt'),('All files', '*.*')))

    if file_name != '':
        f = open(file_name, 'r', encoding='utf-8')
        txt = f.read()
        if txt != None:
            text.delete('1.0', 'end')
            text.insert('end', txt)
            window.title(f'C4311 - TextEditor - {file_name}')

def save_file(event=None):
    file_name = filedialog.asksaveasfilename(title="C4311 - Save file", defaultextension="txt", filetypes=(('Text files', '*.txt'),('All files', '*.*')))
    if file_name != '':
        f = open(file_name, 'w', encoding='utf-8')
        txt = text.get('1.0', 'end')
        f.write(txt)
        messagebox.showinfo("C4311 - TextEditor", 'Файл записаний')



window = tk.Tk()
window.geometry("600x400+600+200")
window.title("C4311 - TextEditor")


menu = tk.Menu()
window.config(menu=menu)

img_open = tk.PhotoImage(file='folder-open-outline-custom.png')
img_save = tk.PhotoImage(file='content-save-settings-outline-custom.png')


file_menu = tk.Menu(tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open..", image=img_open, compound='left', command=open_file, accelerator='Ctrl+O')
file_menu.add_command(label="Save as..", image=img_save, compound='left', command=save_file, accelerator='Ctrl+S')
file_menu.add_separator()
file_menu.add_command(label="Exit")
menu.add_cascade(label="File", menu=file_menu)


about_menu = tk.Menu(tearoff=0)
about_menu.add_command(label="Help")
about_menu.add_command(label="About")
menu.add_cascade(label="Help", menu=about_menu)


text = tk.Text()
text.pack(fill='both', expand=1)

window.bind('<Control-o>', open_file)
window.bind('<Control-s>', save_file)



window.mainloop()

