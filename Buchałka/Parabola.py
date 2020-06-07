import tkinter


def parabola(x):
    y = x * x
    return y

main_window = tkinter.Tk()

main_window.title("Parabaola")
main_window.geometry("640x480")

canvas = tkinter.Canvas(main_window, width=640, height=480)
canvas.grid(row=0, column=0)

for x in range(-100, 100):
    y = parabola(x)
    print(y)

main_window.mainloop()
