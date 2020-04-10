import tkinter as tk
import tkinter.font as font
import speech_recognition as sr
import time
import RPi.GPIO as g
g.setmode(g.BOARD)
g.setup(3,g.OUT)#led
g.setup(5,g.OUT)#motor
g.output(3,False)
g.output(5,False)
r = sr.Recognizer()
HEIGHT = 425
WIDTH = 640
root = tk.Tk()
root.title("ALEXA")
def change():
    #global label2
    #label2.lift()
    global entry,s,r
    #entry.config(text="Say Something")
    
    
    with sr.Microphone(device_index=None,sample_rate=48000,chunk_size=2048) as source:
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        audio = r.listen(source)
        print("time up")
        #label2.lower()
        try:
         text1 = r.recognize_google(audio)
        except:
         print("error")
    entry.config(text=text1)

def cmd(text):
    text2 = text.lower()
    if(text2=="light on" or text2=="led on"):
        g.output(3,True)
        return "turning lights on"
    elif(text2=="light off" or text2=="led off"):
        g.output(3,False)
        return "turning lights off"
    elif(text2=="fan on" or text2=="motor on"):
        g.output(5,True)
        return "turning fan on"
    elif(text2=="fan off" or text2=="motor off"):
        g.output(5,False)
        return "turning fan off"
    else:
        return "invlid commnd"
    
def com():
    global entry
    s = cmd(entry['text'])
    print(s)
def mix():
    change()
    com()
         
    
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.place()

#background_image = tk.PhotoImage(file='alexaaa.png')
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)


myFont = font.Font(size=40)
myFont2 = font.Font(size=28)
label=tk.Label(text="ALEXA",fg='white',bg='#00008b')
label.place(relx=0.434,rely=0)
label['font'] = myFont

label2=tk.Label(text="Recording!!!",fg='red',bg='#00008b')
label2.place(relx=0.431,rely=0.15)
label2['font'] = myFont2
label2.lower()

lower_frame = tk.Frame(root, bg='#80c1ff',bd=1)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.25, relheight=0.1, anchor='n')


button2=tk.Button(lower_frame,text ="START",command=mix)
button2.place(relx=0.02,rely=0.1,relheight=0.8,relwidth=0.95)

#button = tk.Button(lower_frame, text="STOP")
#button.place(relx=0.52,rely=0.1 ,relheight=0.8, relwidth=0.46)


frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.45, relwidth=0.25, relheight=0.25, anchor='n')


entry = tk.Label(frame,text="led on", font=40)
entry.place(relwidth=1, relheight=1)

root.mainloop()
