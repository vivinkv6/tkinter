import tkinter as tk

# Build Form using tkinter

window= tk.Tk()

window.geometry("500x500")

window.title("Simple Form")

# labels
name= tk.Label(window,text="Enter Name:").place(x=50,y=50)
age= tk.Label(window,text="Enter Age: ").place(x=50,y=80)
email= tk.Label(window,text="Enter Email: ").place(x=50,y=110)
gender= tk.Label(window,text="Gender").place(x=50,y=140)
qualification= tk.Label(window,text="Skills").place(x=50,y=170)

# widgets
inputName= tk.Entry(window).place(x=130,y=50)
inputAge= tk.Entry(window).place(x=130,y=80)
inputEmail= tk.Entry(window).place(x=130,y=110)
genderMale= tk.Radiobutton(window,text="Male",value=1).place(x=125,y=138)
genderFeMale= tk.Radiobutton(window,text="Female",value=2).place(x=180,y=138)
genderTransgender= tk.Radiobutton(window,text="Transgender",value=3).place(x=245,y=138)
qualificationOne= tk.Checkbutton(window,text="C").place(x=55,y=200)
qualificationTwo= tk.Checkbutton(window,text="C++").place(x=55,y=230)
qualificationThree= tk.Checkbutton(window,text="Java").place(x=55,y=260)
qualificationFour= tk.Checkbutton(window,text="JavaScript").place(x=55,y=290)
qualificationTwo= tk.Checkbutton(window,text="Python").place(x=55,y=320)
btn= tk.Button(text="Submit").place(x=250,y=380)


window.mainloop()