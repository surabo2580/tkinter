import cv2
import numpy as np
from tkinter import *
from PIL import Image,ImageTk
import datetime

def TakePhoto():
    image = Image.fromarray(img1)
    time = str(datetime.datetime.now().today()).replace(":"," ")+".jpg"
    image.save(time)
    


root = Tk()
root.geometry("700x640")
root.configure(bg="black")
root.name= "Facegenie Camera v1.0"
Label(root,text="Face genie v1.0",font=("times new roman",30,"bold"),bg="black",fg="red").pack()
f1 = LabelFrame(root,bg="red")
f1.pack()
L1 = Label(f1,bg="red")
L1.pack()

cap = cv2.VideoCapture(0)
Button(root,text="snapshot",font=("times new roman",30,"bold"),bg="black",fg="red",command=TakePhoto).pack()



while True:
    img = cap.read()[1]
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img1))
    L1['image'] = img
    root.update()
    
cap.release()
