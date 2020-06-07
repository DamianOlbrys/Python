import tkinter

main_window = tkinter.Tk()

main_window.title("Tytuł")
main_window.geometry("640x480+8+400")

label = tkinter.Label(main_window, text="Hello Word")
label.pack(side='top')

canvas = tkinter.Canvas(main_window, relief='raised', borderwidth=1)
canvas.pack(side='right')

main_window.mainloop()