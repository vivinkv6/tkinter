import tkinter as tk


window=tk.Tk()

window.title("France Flag")
window.geometry("500x500")


frame1=tk.Frame(master=window,bg="blue",width=100,height=200)
frame1.pack(fill=tk.X,side=tk.LEFT)

frame2=tk.Frame(master=window,bg="white",width=100,height=200)
frame2.pack(fill=tk.X,side=tk.LEFT)

frame3=tk.Frame(master=window,bg="red",width=100,height=200)
frame3.pack(fill=tk.X,side=tk.LEFT)






window.mainloop()
