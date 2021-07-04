"""
A GUI program that stores the following book information:
1. Title
2. Author
3. Year Published
4. ISBN Number

The user can:
1. view all records
2. search an entry
3. add entry
4. update  entry
5. delete an entry
6. close the program
"""
from tkinter import *
import backend

def view_command():
    listBox.delete(0, END)
    for row in backend.viewAll():
        listBox.insert(END, row)

def search_command():
    listBox.delete(0, END)
    for row in backend.search(titleText.get(), authorText.get(), yearText.get(), isbnText.get()):
        listBox.insert(END, row)

def add_command():
    listBox.delete(0, END)
    backend.addEntry(titleText.get(), authorText.get(), yearText.get(), isbnText.get())
    listBox.insert(END, {titleText.get(), authorText.get(), yearText.get(), isbnText.get()})

def get_selected_row(event):
    try:
        global selected_tuple
        index = listBox.curselection()[0]
        selected_tuple=listBox.get(index)
        titleEntry.delete(0, END)
        titleEntry.insert(END, selected_tuple[1])

        authorEntry.delete(0, END)
        authorEntry.insert(END, selected_tuple[2])

        yearEntry.delete(0, END)
        yearEntry.insert(END, selected_tuple[3])

        isbnEntry.delete(0, END)
        isbnEntry.insert(END, selected_tuple[4])

    except IndexError:
        pass

def delete_command():
    backend.deleteRecords(selected_tuple[0])

def update_command():
    backend.updateEntry(selected_tuple[0], titleText.get(), authorText.get(), yearText.get(), isbnText.get())

def close_command():
    window.destroy()


# Creating an instance of Tk frame
window = Tk()

# Changing Title of Window
window.title("ABC BOOK DEPOT")

# fixing size of window
window.minsize(400, 300)
window.maxsize(400, 300)

# Adding Labels
titleLabel = Label(window, text="Title")
titleLabel.grid(row=0, column=0)

authorLabel = Label(window, text="Author")
authorLabel.grid(row=1, column=0)

yearLabel = Label(window, text="Year")
yearLabel.grid(row=2, column=0)

isbnLabel = Label(window, text="ISBN")
isbnLabel.grid(row=3, column=0)

# Adding Textfields
titleText = StringVar()
titleEntry = Entry(window, textvariable=titleText)
titleEntry.grid(row=0, column=2)

authorText = StringVar()
authorEntry = Entry(window, textvariable=authorText)
authorEntry.grid(row=1, column=2)

yearText = StringVar()
yearEntry = Entry(window, textvariable=yearText)
yearEntry.grid(row=2, column=2)

isbnText = StringVar()
isbnEntry = Entry(window, textvariable=isbnText)
isbnEntry.grid(row=3, column=2)

# Adding a List Box
listBox = Listbox(window, height=6, width=40)
listBox.grid(row=6, column=0, rowspan=8, columnspan=4)

# Adding a scroll bar
scrollBar = Scrollbar(window)
scrollBar.grid(row=6, column=4, rowspan=8)

# configuring list box and scroll bar
listBox.configure(yscrollcommand=scrollBar.set)
scrollBar.configure(command=listBox.yview)

# binding function to widget
listBox.bind('<<ListboxSelect>>', get_selected_row)

# Adding buttons
viewButton = Button(window, text="View All", width=12, command=view_command)
viewButton.grid(row=6, column=5)

searchButton = Button(window, text="Search Entry", width=12, command=search_command)
searchButton.grid(row=7, column=5)

addButton = Button(window, text="Add Entry", width=12, command=add_command)
addButton.grid(row=8, column=5)

updateButton = Button(window, text="Update", width=12, command=update_command)
updateButton.grid(row=9, column=5)

deleteButton = Button(window, text="Delete", width=12, command=delete_command)
deleteButton.grid(row=10, column=5)

closeButton = Button(window, text="Close", width=12, command=close_command)
closeButton.grid(row=11, column=5)

# Running Tkinter Event loop
window.mainloop()