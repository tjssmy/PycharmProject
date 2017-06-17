from tkinter import Tk, ttk


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        nb = ttk.Notebook(master)
        page1 = ttk.Frame(nb)

        label = ttk.Label(page1, text="This is our first GUI!")
        label.pack()

        greet_button = ttk.Button(page1, text="Greet", command=self.greet)
        greet_button.pack()

        close_button = ttk.Button(page1, text="Close", command=master.quit)
        close_button.pack()

        page2 = ttk.Frame(nb)

        label = ttk.Label(page2, text="Page 2")
        label.pack()

        nb.add(page1, text='One')
        nb.add(page2, text='Two')

        nb.pack(expand=1, fill="both")

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
