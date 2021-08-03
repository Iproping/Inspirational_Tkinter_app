import tkinter as tk
from tkinter import font
import random

HEIGHT = 500
WIDTH = 600

quotes = ["Love For All, Hatred For None. – Khalifatul Masih III",
"Change the world by being yourself. – Amy Poehler",
"Every moment is a fresh beginning. – T.S Eliot",
"Never regret anything that made you smile. – Mark Twain",
"Everything you can imagine is real. – Pablo Picasso",
"Whatever you do, do it well. – Walt Disney",
"What we think, we become. – Buddha",
"Reality is wrong, dreams are for real. – Tupac"]


root = tk.Tk()

def update():
    label.config(text = random.choice(quotes))




canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = "orange", bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.50, relheight = 0.1, anchor = "n")

button = tk.Button(frame, text = "Inspiration", font = ("Courier", 10), command = update) 
button.place(relx = 0.35, relheight = 1, relwidth = 0.3)

lower_frame = tk.Frame(root, bg = "orange", bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 1, relheight = 0.6, anchor = "n")

label = tk.Label(lower_frame, font = ("Courier", 10))
label.place(relwidth = 1., relheight = 1) 




root.mainloop() 
