from tkinter import *
from comutations import *
from PIL import ImageTk,Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def clicked():
    bar = FigureCanvasTkAgg(run(par1_var, par2_var, par3_var), window).get_tk_widget()
    bar.grid(row=0, column=10, columnspan=6, rowspan=11)

window = Tk()
window.title("Assignment")
window.geometry('1280x720')
par1_var = IntVar()
par1_var.set(2)
par2_var = IntVar()
par2_var.set(0)
par3_var = IntVar()
par3_var.set(12)
#bg = PhotoImage(file = "/Users/nm/PycharmProjects/DEH/venv/alexander-tormasov.png")
#back = Label(image=bg)
#back.grid()
bar = FigureCanvasTkAgg(run(par1_var, par2_var, par3_var), window).get_tk_widget()
bar.grid(row=0, column=10, columnspan=6, rowspan=11)
txt = Entry(window, width=10, text=par1_var)
txt.grid(row=4, column=1)
lbl = Label(window, text="x0", font=("Arial Bold", 15))
lbl.grid(row=5, column=1)
txt = Entry(window, width=10, text=par2_var)
txt.grid(row=6, column=1)
lbl = Label(window, text="y0", font=("Arial Bold", 15))
lbl.grid(row=7, column=1)
txt = Entry(window, width=10, text=par3_var)
txt.grid(row=8, column=1)
lbl = Label(window, text="X", font=("Arial Bold", 15))
lbl.grid(row=9, column=1)
btn = Button(window, text="Plot", bg="white", fg="red", command=clicked)
btn.grid(row=10, column=1)
# chk = Checkbutton(window, text='graph1')
# chk.grid(row=7, column=1)
# chk = Checkbutton(window, text='graph2')
# chk.grid(row=8, column=1)
# chk = Checkbutton(window, text='graph3')
# chk.grid(row=9, column=1)
# chk_state = IntVar()
# chk_state.set(0) # False
# chk_state.set(1) # True


window.mainloop()
