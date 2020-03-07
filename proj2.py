from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import directoryTools as dirTools


class MainWindow:

    def __init__(self, master):
        # Variables
        self.dirInputValue = StringVar()
        self.dirContents = []

        # Main Frame
        self.main_frame = LabelFrame(master, text='Rename directories', padx=20, pady=20)
        self.main_frame.grid(row=0, column=0, sticky=(N, W, E, S))

        self.dir_frame = LabelFrame(self.main_frame, text='Get the Directory', padx=20, pady=20)
        self.dir_frame.grid(row=0, column=0, sticky=(N, W, E, S))
        self.dir_frame['borderwidth'] = 2
        self.dir_frame['relief'] = 'sunken'

        # User Inputs
        self.dirLabel = ttk.Label(self.dir_frame, text="Enter the starting directory", anchor=N)
        self.dirLabel.grid(row=0, column=0, sticky=W)

        self.dirInput = ttk.Entry(self.dir_frame, width=32, textvariable=self.dirInputValue)
        self.dirInput.grid(row=1, column=0, sticky=W)

        self.dirButton = ttk.Button(self.dir_frame, text='Find Directory...', command=self.get_directory_name)
        self.dirButton.grid(row=1, column=1, sticky=W)

        self.dirListButton = ttk.Button(self.dir_frame, text='Get Directory Contents', command=self.populate_tree)
        self.dirListButton.grid(row=2, column=0, pady=20, sticky=W)

        # Tree
        self.tree_frame = LabelFrame(self.main_frame, text='See the files', padx=10, pady=10)
        self.tree_frame.grid(row=0, column=1, sticky=(N, W, E, S))
        self.tree_frame['borderwidth'] = 2
        self.tree_frame['relief'] = 'sunken'

        self.treeWindow = ttk.Treeview(self.tree_frame)
        self.treeWindow.grid(row=0, column=0) # , rowspan=6)

    # Functions
    def get_directory_name(self):
        dirname = filedialog.askdirectory()
        self.dirInputValue.set(dirname)

    def populate_tree(self):
        print('populating tree')
        dir_tool = dirTools.DirectoryTools()
        dir_contents = dir_tool.get_directory_contents(self.dirInputValue.get())
        for file in dir_contents:
            tree_id = self.treeWindow.insert('', 'end', text=file)
            print(file)


root = Tk()
root.geometry('800x500')
main = MainWindow(root)
root.mainloop()
