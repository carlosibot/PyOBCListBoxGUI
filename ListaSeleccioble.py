import tkinter

window = tkinter.Tk()
label = tkinter.Label(window, text='¿En que continente vives?')
label.grid(column=0, row=0, pady=5, padx=5)
lista = ['Africa', 'America','Asia', 'Europa', 'Oceania']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, listvariable=lista_items, height=5, selectmode='browse')
listbox.grid(column=0,row=1,sticky=tkinter.S)

window.mainloop()