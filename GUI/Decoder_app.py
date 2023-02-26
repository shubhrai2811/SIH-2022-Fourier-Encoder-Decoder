from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter
from tkinter.messagebox import showinfo
def openWavFile():
    wave_filepath= filedialog.askopenfile(title="Select any wave file!", 
                filetypes= (("Wave Files","*.wav"),("All Files","*.*")))
    print(wave_filepath)
root= Tk() #initializing a tkinter app window
root.title("Decoder")
root.geometry("640x480+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)
#Icon
image_icon= PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)
Label(root, text= "Decoder", font=("Acumin Variable Concept",20,"bold"), 
                        bg= "#f4fdfe", foreground="#a30000").place(x=250,y=20)
Frame(root, width=400, height=2, bg ="#f3f5f6").place(x=25, y=80)
# For Wave file accessing button
wave = PhotoImage(file="wave_1.png")
op_wave= Button(root, image=wave, bg= "#a3f000",bd =0.5, command=openWavFile)
op_wave.place(x=250, y=100)
# For placing the text describing above button
Label(root, text= "Open Wave File", font=("Acumin Variable Concept",12,"bold"), 
                        bg= "#f4fdfe", foreground="#a30000").place(x=250,y=200)
play=PhotoImage(file="play.png")
#Giving the progress bar
play_button = Button(root, image=play,bg="#f4fdfe", bd=0)
play_button.place(x=450, y=300)
prog_ta= Text(root, height=10, width=30)
prog_ta.pack(expand= True)
prog_ta.config(state="disabled")
prog_ta.place(x=50, y=250)
root.mainloop()