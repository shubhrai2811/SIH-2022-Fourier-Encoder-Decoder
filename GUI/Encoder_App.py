from tkinter import * 
from tkinter import filedialog
from playsound import playsound

def openMultFile():
    mult_filepath= filedialog.askopenfile(title="Select any multimedia file!", 
                filetypes= (("Image Files","*.jpg, *.jpeg, *.png"),("Text Files","*.txt"),("Video Files","*.mp4"),("All Files","*.*")))
root= Tk()
root.title("Encoder")
root.geometry("640x480+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)
#Icon
image_icon= PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)
Label(root, text= "Encoder", font=("Acumin Variable Concept",20,"bold"), 
                        bg= "#f4fdfe", foreground="#a30000").place(x=250,y=20)
Frame(root, width=400, height=2, bg ="#f3f5f6").place(x=25, y=80)
#For multimedia file accessing button
multimedia = PhotoImage(file="accept_file.png", )
op_mult= Button(root, image=multimedia, bg= "#a3f000",bd=0.5,command=openMultFile)
op_mult.place(x=250, y=100)
# For placing the text describing above
Label(root, text= "Open Multimedia File", font=("Acumin Variable Concept",12,"bold"), 
                        bg= "#f4fdfe", foreground="#a30000").place(x=220,y=170)
play=PhotoImage(file="play.png")
play_button = Button(root, image=play,bg="#f4fdfe", bd=0)
play_button.place(x=450, y=300)
prog_ta= Text(root, height=10, width=30)
prog_ta.pack(expand= True)
prog_ta.config(state="disabled")
prog_ta.place(x=50, y=250)
root.mainloop()

def play_sound(filename):
    playsound(filename)
