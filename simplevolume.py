# Visit Our facebook page: Uncle Engineer
# www.facebook.com/UncleEngineer
# www.uncle-engineer.com/python

from tkinter import *
from tkinter import ttk

def Cal():
    bw = float(bwidth.get())
    bd = float(bdepth.get())
    bl = float(blength.get())
    volumn = "Volume: {:.3f} m³".format(bw * bd * bl)
    result.set(volumn)

GUI = Tk()
GUI.title('Uncle Engineer Volume Calculator')
GUI.geometry('500x500')

# Variable
bwidth = StringVar()
bdepth = StringVar()
blength = StringVar()
result = StringVar()

# Image
bg = PhotoImage(file='bg.png')
# Image Label
I1 = ttk.Label(GUI, image=bg)
I1.pack(padx=10,pady=5)

# Beam Textbox
L1 = ttk.Label(GUI, text= 'Beam width (m)(1)')
L1.pack(padx=10,pady=5)

E1 = ttk.Entry(GUI, textvariable= bwidth)
E1.pack(padx=10,pady=5)

L2 = ttk.Label(GUI, text= 'Beam Depth (m)(2)')
L2.pack(padx=10,pady=5)

E2 = ttk.Entry(GUI, textvariable= bdepth)
E2.pack(padx=10,pady=5)

L3 = ttk.Label(GUI, text= 'Beam Length (m)(3)')
L3.pack(padx=10,pady=5)

E3 = ttk.Entry(GUI, textvariable= blength)
E3.pack(padx=10,pady=5)

#Calculate Button
B1 = ttk.Button(GUI, text= 'Cal Volume', command=Cal)
B1.pack()

R1 = ttk.Label(GUI, textvariable= result, font=('tohama',20))
R1.pack(padx=10,pady=5)

GUI.mainloop()
