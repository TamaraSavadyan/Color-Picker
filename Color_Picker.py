from tkinter import *
from tkinter import colorchooser


root = Tk()
root.geometry('330x160')
root.title('Color picker!')

fg_color = '#000000'
bg_color = '#ffffff'


def pickColor_Bg():
    global bg_color, fg_color
    # pick BG color
    bg_color = colorchooser.askcolor()[1]
    bg_entry.delete(0, END)
    # Display color with it's hex code
    bg_entry.insert(0, 'Hex code for Bg: ' + str(bg_color))

    # Display colors of BG and FG (how they look together)
    Label(root, text='U picked that Bg color and that Fg color!', fg=fg_color, bg=bg_color).place(x=10, y=60,
                                                                                                  width=300, height=50)


def pickColor_Fg():
    global bg_color, fg_color
    # pick FG color
    fg_color = colorchooser.askcolor()[1]
    fg_entry.delete(0, END)
    fg_entry.insert(0, 'Hex code for Fg: ' + str(fg_color))

    # Display colors of BG and FG (how they look together)
    Label(root, text='U picked that Bg color and that Fg color!', fg=fg_color, bg=bg_color).place(x=10, y=60,
                                                                                                  width=300, height=50)


def clear():
    fg_entry.delete(0, END)
    bg_entry.delete(0, END)
    Label(root, text='U picked that Bg color and that Fg color!', fg='#f0f0f0', bg='#f0f0f0').place(x=10, y=60,
                                                                                                    width=300,
                                                                                                    height=50)


# Place entries and labels on the screen
fg_entry = Entry(root)
fg_entry.place(x=160, y=30, width=155)

bg_entry = Entry(root)
bg_entry.place(x=160, y=10, width=155)
Label(root, text='U picked that Bg color and that Fg color!', fg='#f0f0f0', bg='#f0f0f0').place(x=10, y=60,
                                                                                                width=300, height=50)

# Button to BG pick color
Bg_Color_btn = Button(root, text='Pick Bg color', command=pickColor_Bg)
Bg_Color_btn.place(x=10, y=10, width=150, height=20)

# Button to FG pick color
Fg_Color_btn = Button(root, text='Pick Fg color', command=pickColor_Fg)
Fg_Color_btn.place(x=10, y=30, width=150, height=20)

# Button to clear screen
clear_btn = Button(root, text='Clear', command=clear)
clear_btn.place(x=10, y=120, width=100, height=25)


root.resizable(False, False)
root.mainloop()
