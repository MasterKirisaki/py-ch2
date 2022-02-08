def triangle():
      
      

from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมหาพื้นที่สามเหลี่ยม โดย กฤติน พรธรรมรักษ์")
base = StringVar()
high = StringVar()
area = StringVar()

lb1 = Label(main, text="คะแนนเก็บ:", font=("Tahoma" ,18) )
lb1.place(x=20, y=20)
tbl1 = Entry(main, textvariable=base)
tbl1.place(x=220, y=30)

lb2 = Label(main, text="คะแนนกลางภาค:", font=("Tahoma" ,18) )
lb2.place(x=20, y=80)
tbl2 = Entry(main, textvariable=high)
tbl2.place(x=220, y=90)

lb3 = Label(main, text="คะแนนปลายภาค:", font=("Tahoma" ,18) )
lb3.place(x=20, y=140)
tbl3 = Entry(main, textvariable=high)
tbl3.place(x=220, y=150)

lb4 = Label(main, text="จิตพิสัย:", font=("Tahoma" ,18) )
lb4.place(x=20, y=200)
tbl4 = Entry(main, textvariable=high)
tbl4.place(x=220, y=210)

lb5 = Label(main, text="คำตอบ:", font=("Tahoma" ,18) )
lb5.place(x=20, y=260)
tbl5 = Entry(main, textvariable=high)
tbl5.place(x=220, y=270)

btn = Button(main, text="คำนวณ", font=("Tahoma" ,18), command= triangle)
btn.place(x=400, y=10)