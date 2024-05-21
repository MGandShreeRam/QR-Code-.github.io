import qrcode
from tkinter import *
import os
from PIL import Image,ImageTk
from random import randint
root = Tk()


Img = Image.open(r"C:\Users\King\Desktop\New folder\infrared spectroscopy.png")
IMg4 = Img.resize((500,500))
img = ImageTk.PhotoImage(IMg4)

image_list = [img]
my_label= Label(image=img)
my_label.grid(row=0, column=0, columnspan=3)
number = 326961941

def qr_generator():
    global number
    global image_list
    qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size=50,border=10,)
    
    number += randint(1,10)
    
    code = "A1SX0472G-GYNO0010-1023R09MA0-     1649.00-8907639692533-1009-200524964-0"
    qr_code = code + str(number)
    qr.add_data(qr_code)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save("infrared spectroscopy.png")
    Img = Image.open("infrared spectroscopy.png")
    IMg4 = Img.resize((500,500))
    img = ImageTk.PhotoImage(IMg4)
    
    my_label= Label(image=img)      
    my_label.grid(row=0, column=0, columnspan=3)
    image_list.append(img)
    


# Creating Forward function for forward button
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    
    button_forward = Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back = Button(root, text="<<", state=NORMAL, command=lambda:back(image_number))
    
    # if image_number == 4:
    #     button_forward = Button(root, text=">>", state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    qr_generator()
    
    
# Creating back function for back button
def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    
    button_forward = Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back = Button(root, text="<<", state=NORMAL, command=lambda:back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

button_back = Button(root, text="<<", state=DISABLED, command=back)
button_exit = Button(root, text="Exit Program",command=exit)
button_forward = Button(root, text=">>", command=lambda:forward(0))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
root.mainloop()
