import tkinter as tk
import numpy as np

class Connect4:

    def __init__(self):
        self.Board()

    class Board(tk.Frame):

        def __init__(self):
            self.columns = 7
            self.rows = 6
            self.width = 600
            self.height = self.width*self.rows/self.columns

            

            self.root = tk.Tk()
            self.root.title("ConnectFour")


            self.create_board()

            self.root.mainloop()
        
        def create_board(self):

            # Main board
            self.canvas_board = tk.Canvas(self.root, width=self.width, height=self.height, background='darkblue')

            self.canvas_board.grid(column=1, row=0)

            # Holes
            self.width_circle = self.width/self.columns
            self.height_circle = self.width_circle

            x0 = 0
            
            for i in range(self.columns):
                y0 = 0
                for j in range(self.rows):
                    self.canvas_board.create_oval(x0,y0, x0+self.width_circle, y0+self.height_circle, fill="white", outline="black")
                    y0 += self.height_circle
                x0 += self.width_circle

            self.spaces = np.zeros((6,7))
            self.column_index = np.zeros((6,1))

            # Main Buttons Frame
            self.controls_frame = tk.Frame(self.root, relief="groove")
            self.controls_frame.grid(column=0, row=0, padx=2, pady=2)

            # AI Level
            ai_label = tk.Label(self.controls_frame, text="AI Level:")
            ai_label.grid(column=0, row=0, sticky=tk.W)

            self.variable_ai_lebel = tk.IntVar()
            self.variable_ai_lebel.set(1)
            self.ai_entry = tk.Entry(self.controls_frame, width=10, textvariable=self.variable_ai_lebel)
            self.ai_entry.grid(column=0, row=1)

            # Start CPU

            self.start_cpu_button = tk.Button(self.controls_frame, text="Start CPUs", width=10)
            self.start_cpu_button.grid(column=0, row=2, padx=2, pady=2)

            # Restart
            self.restart_button = tk.Button(self.controls_frame, text="Restart", width=10)
            self.restart_button.grid(column=0, row=3, padx=2, pady=2)

            # Undo
            self.undo_button = tk.Button(self.controls_frame, text="Undo", width=10)
            self.undo_button.grid(column=0, row=4, padx=2, pady=2)

            # Messages
            
            self.variable_message = tk.StringVar()
            self.variable_message.set("Waiting to start...")
            self.message_entry = tk.Entry(self.root, textvariable=self.variable_message, state="readonly")
            self.message_entry.grid(column=0, row=2, columnspan=2, sticky=tk.W+tk.E, padx=2, pady=2)


    
    class Chip(tk.Canvas):

        def __init__(self):
            pass

Connect4()
