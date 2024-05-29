import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Add Score")
        label.pack(side="top", fill="both", expand=True)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Graphic")
        label.pack(side="top")
        
        #data1 = {
        #    "Dates": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        #    "Scores": [560, 540, 610, 590, 605, 580, 503, 630, 576, 605],
        #    }
        #df1 = pd.DataFrame(data1)
        
        figure1 = plt.Figure(figsize=(5, 4), dpi=100)
        #ax1 = figure1.add_subplot(111)
        #bar1 = FigureCanvasTkAgg(figure1, self)
        #bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        #df1 = df1[["Dates", "Scores"]].groupby("Dates").sum()
        #df1.plot(kind="bar", legend=True, ax=ax1)
        #ax2 = table[1].plot(secondary_y=True,color='red', ax=ax1)
        #ax1.set_title("Last 10 scores")
        
        dates = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        scores = [560, 540, 610, 590, 605, 580, 503, 630, 576, 605]
        ten_percent = [90, 95, 88, 89, 92, 90, 89, 91, 96, 87]
        
        plt.bar(dates, scores, tick_label = dates, width = 0.8, color = 'blue')
        plt.plot(dates, ten_percent, label = r'% of 10')

        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('My bar chart!')
        plt.show()


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Convert")
       label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Add Score", command=p1.show)
        b2 = tk.Button(buttonframe, text="Graphic", command=p2.show)
        b3 = tk.Button(buttonframe, text="Convert", command=p3.show)
        close_button = tk.Button(buttonframe, text="Close", command=root.quit)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        close_button.pack(side="right")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("500x600")
    root.mainloop()