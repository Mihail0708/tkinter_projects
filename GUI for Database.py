from tkinter import *
import sqlite3

root = Tk()
root.title('Checkboxes')
root.geometry('300x500')

# Create the table
# cursor.execute("""CREATE TABLE addresses(
# first_name text,
# last_name text,
# address text,
# city text,
# state text,
# zipcode integer)""")


def save():
    # Creating a database or connect to one
    connection = sqlite3.connect('address_book.db')

    # Create cursor
    cursor = connection.cursor()

    record_id= delete_box.get()

    cursor.execute("""UPDATE addresses SET 
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode
    WHERE oid = :oid""",
                   {
                       'first': f_name_editor.get(),
                       'last': l_name_editor.get(),
                       'address': address_editor.get(),
                       'city': city_editor.get(),
                       'state': state_editor.get(),
                       'zipcode': zipcode_editor.get(),
                       'oid': record_id
                   })

    # Commit changes
    connection.commit()

    # Close connection
    connection.close()

    editor.destroy()


def update():
    global editor
    editor = Tk()
    editor.title('Update a record')
    editor.geometry('300x200')\

    # Creating a database or connect to one
    connection = sqlite3.connect('address_book.db')

    # Create cursor
    cursor = connection.cursor()

    record_id = delete_box.get()

    # get info from DB
    cursor.execute('SELECT * FROM addresses WHERE oid =' + record_id)
    records = cursor.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create Text Box Labels
    f_name_label_editor = Label(editor, text='First name')
    f_name_label_editor.grid(row=0, column=0)
    l_name_label_editor = Label(editor, text='Last name')
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text='Address')
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text='City')
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text='State')
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text='Zipcode')
    zipcode_label_editor.grid(row=5, column=0)

    # loop through records
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create save button
    save_btn = Button(editor, text='Save', command=save)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, ipadx=49)


def delete():
    # Creating a database or connect to one
    connection = sqlite3.connect('address_book.db')

    # Create cursor
    cursor = connection.cursor()

    # Delete a record
    cursor.execute('DELETE from addresses WHERE oid=' + delete_box.get())

    # Commit changes
    connection.commit()

    # Close connection
    connection.close()

    # Clear delete box
    delete_box.delete(0, END)


def submit():
    # Creating a database or connect to one
    connection = sqlite3.connect('address_book.db')

    # Create cursor
    cursor = connection.cursor()

    # Insert into table
    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                   {
                       'f_name': f_name.get(),
                       'l_name': l_name.get(),
                       'address': address.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zipcode': zipcode.get()}
                   )

    # Commit changes
    connection.commit()

    # Close connection
    connection.close()

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def get_info():
    # Creating a database or connect to one
    connection = sqlite3.connect('address_book.db')

    # Create cursor
    cursor = connection.cursor()

    # get info from DB
    cursor.execute('SELECT *, oid FROM addresses')
    records = cursor.fetchall()

    result = ''
    for record in records:
        for el in record:
            result += str(el) + ' '
        result += '\n'

    result_label = Label(root, text=result)
    result_label.grid(row=11, column=0, columnspan=2, pady=(20, 0))

    # Commit changes
    connection.commit()

    # Close connection
    connection.close()


# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1)

# Create Text Box Labels
f_name_label = Label(root, text='First name')
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text='Last name')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text='Select ID')
delete_box_label.grid(row=8, column=0)

# Create submit button
submit_btn = Button(root, text='Submit', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, ipadx=50)

# Create get button
get_btn = Button(root, text='Get info', command=get_info)
get_btn.grid(row=7, column=0, columnspan=2, pady=10, ipadx=48)

# Delete button
delete_btn = Button(root, text='Delete', command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, ipadx=52)

# Update button
update_btn = Button(root, text='Update', command=update)
update_btn.grid(row=10, column=0, columnspan=2, pady=10, ipadx=49)


root.mainloop()

