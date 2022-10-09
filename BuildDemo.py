import tkinter as tk
import cv2
from PIL import Image, ImageTk

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root.geometry('1000x720')
root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)

TitleLabel = tk.Label(text="Drowsiness detection for driver",font=("bold", 22))
State = tk.Label(text="State: ",font=("bold", 22))
TestState = tk.Label(text="open",font=("bold", 22))
ScoreText = tk.Label(text="State: ",font=("bold", 22))
ScoreNum = tk.Label(text="15 ",font=("bold", 22))

def buttons():
    for i in "Connect", "real-time", "Stop real-time", "Send data":
        b = tk.Button(master=root, text=i, font=("bold", 14))
        yield b
        
b1, b2, b3, b4 = buttons()

def configureApp():
    TitleLabel.grid(row=0, column=0,pady=10)
    lmain.grid(row=1, column=0, rowspan=4)
    State.grid(row=5,column=0, sticky = "w")
    TestState.grid(row=5,column=0,sticky = "w", padx=100)
    Score.
    rowPlus=0
    for i in [b1, b2, b3, b4]:
        rowPlus += 1
        i.grid(row = rowPlus, column= 1)


def show_frame():
    while(True):
        _, frame = cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        root.update()

    
configureApp()
show_frame()
cap.release()
cv2.destroyAllWindows()