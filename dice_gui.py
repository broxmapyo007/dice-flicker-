from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import random
from time import *

root=Tk()
root.geometry("800x800")
root.title("DICE (+_ +)	")
root.config(bg="sky blue")
def fil(c):
	fill=f"/storage/emulated/0/code/dicegui/dice{c}.jpeg"
	return ImageTk.PhotoImage(Image.open(fill))
	
def spin():
	global dic_p,bu,l,res
	s=list(dic_p)
	cho=0
	def flick():
		op=0
		cho=random.randint(0,6)
		if len(s)!=0:
			s.pop()
			l.config(image=dic_p[cho])			
			l.after(100,flick)
		op=cho
		l.config(image=dic_p[op])			
		dice["text"]="DICE : "+str(cho)
		if len(s)==0:
			res["text"]="You got :  "+str(cho)
			return 
	flick()
	
	
dic_p=[]
for i in range(7):
	dic_p.append(fil(i))

l=Label(root,image=dic_p[0])
l.pack(side=TOP)

res=Label(root,text="........",font=("roman",20,""),fg="purple",bg="sky blue")
res.place(x=90,y=570)

Label(root,text="FLICK  DICE -->  ",bg="sky blue",font=("arial",10,"bold"),fg="blue").place(x=5,y=400)

dice=Button(root,text="DICE ",fg="yellow" ,bg="red",command=spin,font=('arial',10,'bold'))
dice.place(x=420,y=390)

root.mainloop()