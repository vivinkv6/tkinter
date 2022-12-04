import tkinter as tk


window=tk.Tk()

window.geometry("500x500")
window.title("Todo List")

title=tk.Label(master=window,text="TODO LIST",font=("arial",35,"bold")).pack()

task=tk.Entry(master=window,width=40).pack()

btn=tk.Button(master=window,text="ADD",font=("arial",15,"bold"),padx=15).pack()

tasks=tk.Label(text="Task One",font=("arial",10,"bold")).place(x=120,y=150)
window.mainloop()