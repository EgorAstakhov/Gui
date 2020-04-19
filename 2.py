from tkinter import *
from tkinter import ttk
from tkinter import messagebox



def delete():
    selection = languages_listbox.curselection()  
    mes = messagebox.askyesno(title="Вопрос", message="Удалить данные?")  
    if mes == TRUE: 
        languages_listbox.delete(selection[0])



def add():
    new_language = language_entry.get()  
    languages_listbox.insert(0, new_language) 
    writer = open('language.txt', 'a')
    writer.write(' ' + str(new_language))
    writer.close()


root = Tk()
root.title("GUI на Python")


language_entry = Entry(width=40)  
language_entry.grid(column=0, row=0, padx=6, pady=6)
add_button = ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)


languages_listbox = Listbox()
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=W + E, padx=5, pady=5)



writer = open('language.txt', 'a')
writer.write(' ')
writer = open('language.txt')
for line in writer:
    words = line.split()
for i in range(len(words)):
    languages_listbox.insert(END,words[i])
writer.close()

delete_button = ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
