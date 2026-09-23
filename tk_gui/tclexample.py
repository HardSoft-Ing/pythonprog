# To be used for CRT64 python
import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=500, width=600)

# Draw circle
arc_xoffs = 0
coord = 10 + arc_xoffs, 50, 160 + arc_xoffs, 200
C.create_arc(coord, start=0, extent=3*90, fill="red")

# Draw ellipsis 
arc_xoffs = 160 + arc_xoffs
coord = 10 + arc_xoffs, 50, 310 + arc_xoffs, 200
C.create_arc(coord, start=0, extent=3*90, fill="yellow")

coord = 10, 50 + 215, 240, 210 + 215
rec = C.create_rectangle(coord, fill="green")

C.pack()
top.mainloop()