from tkinter import *
from tkinter import ttk
import mathplot_try as mp

window = Tk()
window.title("Archery Companion")
bg_color = "white"
window.configure(background=bg_color)
window.minsize(200, 200)  # width, height
window.geometry("300x300+50+50")

#button = ttk.Button(window, text='Click Me!', style='green/white.TButton')
#button.pack()

# bouton de sortie
button_1 = Button(window, text="Graph", command=mp.main, highlightbackground=bg_color)
button_1.pack()

close_button = Button(window, text="Close", command=window.quit, highlightbackground=bg_color)
close_button.pack()

window.mainloop()