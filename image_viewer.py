from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')


# Create images
my_img1 = ImageTk.PhotoImage(Image.open('pics/coffee.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('pics/picture3.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('pics/picture4.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('pics/picture5.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4]

# Create status bar
status = Label(root, text=f'Image 1 of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E, padx=10)

# Create label and grid
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    # Remove previous image
    my_label.grid_forget()

    # Creating new label with buttons and image
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    # Update the status bar
    status = Label(root, text=f'Image {image_number} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E, padx=10)

    # Disable the button at the last image
    if image_number == 4:
        button_forward = Button(root, text='>>', state=DISABLED)

    # Placing the new image, buttons and status bar
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))
    status = Label(root, text=f'Image {image_number} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E, padx=10)

    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


# Create buttons
button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='Exit', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

# Place buttons and status bar
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1, pady=10)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()
