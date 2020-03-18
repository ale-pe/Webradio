pathjingle = "C:\\Users\\user\\Desktop\\Radio\\Jingle"
pathmusic = "C:\\Users\\user\\Desktop\\Radio\\Musique"
pathpub = "C:\\Users\\user\\Desktop\\Radio\\PUB"
pathTOPH = "C:\\Users\\user\\Desktop\\Radio\\TOPH"


import pygame
from tkinter import *
import time
import os, random
pub = 0
pubstate = 0
jingle = 1;
start = 1;
def check_event(): 
    global jingle
    global pub
    global pubstate
    global pathTOPH
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    if time.strftime("%M", t) == "14":
        if time.strftime("%S", t) == "30":
            if tophactivation.get() == 1 :
                path = pathTOPH
                file = os.path.join(path, random.choice(os.listdir(path)))
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
    if time.strftime("%M", t) == "30":
        if time.strftime("%S", t) == "00":

            playpub()
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            if jingle == 0 :
                print('1')
                playmusic()
            elif jingle == 1 :
                print('2')
                playjingle()
            elif pubstate == 1 :
                pub = pub + 1
                playpub()
    root.after(1000, check_event)
def stop():
    global jingle
    jingle = 2
    pygame.mixer.music.stop()
def jingleonly():
    global jingle
    global pathjingle
    path = pathjingle
    file = os.path.join(path, random.choice(os.listdir(path)))
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    jingle = 2
    now.set("Jingle")
def musiconly():
    global jingle
    global pathmusic
    path = pathmusic
    filec =  random.choice(os.listdir(path))
    file = os.path.join(path,filec)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    jingle = 2
    now.set(filec)
def playpub():
    global pub
    global pubstate
    global jingle
    global pathpub
    if pubactivation.get() == 1:
        if pub == 0:
            pubstate = 1
            jingle = 2
            path = pathpub
            file = os.path.join(path,"1.mp3")
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
        if pub == 1:
            path = pathpub
            file = os.path.join(path,"2.mp3")
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
        if pub == 2:
            path = pathpub
            file = os.path.join(path,"3.mp3")
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
        if pub == 3:
            path = pathpub
            file = os.path.join(path,"4.mp3")
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            pub = 0
            pubstate = 0
            jingle = 0



def playmusic() :
    global jingle
    global pathmusic
    path = pathmusic
    filec =  random.choice(os.listdir(path))
    file = os.path.join(path,filec)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    now.set(filec)
    jingle = 1
def playjingle() :
    global jingle
    global pathjingle
    path = pathjingle
    file = os.path.join(path, random.choice(os.listdir(path)))
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    now.set("Jingle")
    jingle = 0

# --- main ---

pygame.init()    

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

root = Tk()
root['bg']='#40E0D0' # couleur de fond
now = StringVar()


FrameA1 = Frame(root,bg="white",borderwidth=2,relief=GROOVE)
FrameA1.pack(padx=10,pady=10,side=LEFT)
Frame1 = Frame(FrameA1,bg="white",borderwidth=2,relief=GROOVE)
Frame1.pack(padx=10,pady=10,side=LEFT)
Frame2 = Frame(FrameA1,bg="white",borderwidth=2,relief=GROOVE)
Frame2.pack(padx=10,pady=10,side=LEFT)
Button(Frame1,text="Autoplay",fg='navy',command=playjingle).pack(padx=10,pady=10)
Button(Frame1,text="Lancement Jingle",fg='navy',command=jingleonly).pack(padx=10,pady=10)
Button(Frame1,text="Lancement Musique ",fg='navy',command=musiconly).pack(padx=10,pady=10)
Button(Frame1,text="STOP",fg='navy',command=stop).pack(padx=10,pady=10)
pubactivation = IntVar()
pubactivation.set(0) # ON
Checkbutton(Frame1,text="PUB (A chaque xxh30)",variable=pubactivation).pack(side=LEFT,padx=10,pady=10)
tophactivation = IntVar()
tophactivation.set(0) # ON
Checkbutton(Frame1,text="Top Horaire (A chaque xxh00)",variable=tophactivation).pack(side=LEFT,padx=10,pady=10)
Button(Frame2,textvariable=now,fg='navy').pack(padx=10,pady=10)

check_event()
root.mainloop()

pygame.quit()
