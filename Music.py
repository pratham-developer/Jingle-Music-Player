import tkinter as bk
from tkinter import ttk
from ttkthemes import themed_tk as tk
import os
from tkinter import filedialog
import pygame
from tkinter import messagebox
from mutagen.mp3 import MP3
import time as tt

import random as rr








root=tk.ThemedTk()
style=ttk.Style(root)
style.theme_use('scidblue')
root.resizable(width=False, height=False)


pygame.mixer.init()
style.configure('TButton', border=0,borderwidth=0 )
style.configure('Horizontal.TScale', bg=["active","red"], height=100, border=0)

root.title("Jingle Music Player")
root.geometry("900x453")
root.iconbitmap(r'assets\Iconka-Christmas-Wreath-Bells.ico')

v = bk.PhotoImage(file="assets\gash.png")
b=bk.PhotoImage(file="assets\mash.png")

jk=bk.PhotoImage(file="assets\plus.png")
bl=bk.PhotoImage(file="assets\substract.png")

global don
don=False
#functions__________________________________________________________________________________________________________________________________
# Functions___________________________________________________________________________________________________________________

def minimize():
    root.iconify()

def exit1():
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load("assets\Lock.ogg")
    pygame.mixer.music.play()
    root.destroy()

    tt.sleep(0.5)



def exit2():
 global check
 if check==False:

    pygame.mixer.music.pause()
 elif check==True:
     pass

 ask=messagebox.askquestion(title="Jingle Music Player", message="Are you sure you want to quit?", parent=root)
 if ask=="yes":



    exit1()
    quit()
 elif ask=="no":
     if check==False:

         pygame.mixer.music.unpause()
     elif check==True:
         pass



root.protocol("WM_DELETE_WINDOW",exit2 )

def add():
    global add
    add=filedialog.askopenfilenames(title="Choose Files", filetype=[(".mp3", "*.mp3")])
    for entry in add:

        playlist.insert(0, entry)





def delete():
 pqr= playlist.size()
 if pqr==0:
     messagebox.showerror(title="Jingle Music Player", message="The playlist is already empty.",  parent=root)

 elif pqr>0:
  red = messagebox.askquestion(title="Jingle Music Player", message="This will stop the music if currently being played and you will have to play it again. Are you sure you want to proceed?", parent=root)
  if red=="yes":

    sto()
    root.attributes("-disabled", True)

    def dty():

     global don


     don = False
     qr = playlist.size()
     if qr==0:
         me=messagebox.askquestion(title="Jingle Music Player ", message="The playlist is empty. Do you want to leave?", parent=master)
         master.deiconify()
         if me == "yes":
             cheap()
         elif me == "no":
             pass

     else:

      fake.delete('active')
      fake.selection_set(0, None)
      fake.activate(0)
      zara = fake.get(0, 'end')
      playlist.delete(0,'end')

      for m in zara:
         playlist.insert(0, m)

      mala = playlist.get(0, 'end')
      playlist.delete(0,'end')
      for n in mala:
         playlist.insert(0, n)



    def del_all():
         global don
         don=False
         dr = playlist.size()
         if dr == 0:
             dem=messagebox.askquestion(title="Jingle Music Player ", message="The playlist is empty. Do you want to leave?", parent=master)
             master.deiconify()
             if dem=="yes":
                 cheap()
             elif dem=="no":
                 pass

         else:

          fake.delete(0, 'end')
          playlist.delete(0, 'end')


    def cheap():

        master.destroy()
        root.deiconify()
        root.attributes("-disabled", False)


    playlist.selection_clear(0, 'end')


    master=bk.Toplevel()
    master.resizable(width=False, height=False)
    master.geometry("400x300")
    master.iconbitmap(r'assets\Iconka-Christmas-Wreath-Bells.ico')
    master.protocol("WM_DELETE_WINDOW", cheap)

    set = bk.Label(master, text="Select The Files From The Playlist", font=("Arial Black", 10),height=2, width=65)
    set.pack(side="top")
    fake= bk.Listbox(master, height=12, width=65 )
    fake.pack(side="top")
    but = bk.Button(master,image=b,  command=dty)
    but.place(x=120, y=240)

    cri = bk.Label(master, text="Delete", font=("Arial Black", 8))
    cri.place(x=116, y= 280)

    bu2 = bk.Button(master, image=v,  command=del_all)
    bu2.place(x=230, y=240)


    fri = bk.Label(master, text="Delete All", font=("Arial Black", 8))
    fri.place(x=217, y=280)
    team=playlist.get(0, 'end')
    for q in team:
        fake.insert(0, q)

    gemin = fake.get(0, 'end')
    fake.delete(0, 'end')
    for z in gemin:
        fake.insert(0, z)
    fake.selection_set(0, None)
    fake.activate(0)

    master.mainloop()
  elif red=="no":
      pass










global check
check=False




def play_pause():
   if bool(pygame.mixer.music.get_busy())==True:



     try:

        global check




        if check==False:
            pygame.mixer.music.pause()
            check=True

            play.config(image=c)
            pau.config(text="UNPAUSE")
            pau.place(x=623, y= 210)

        elif check==True:
            pygame.mixer.music.unpause()
            check=False


            play.config(image=j)
            pau.config(text="PAUSE")
            pau.place(x=632, y=210)

     except :

        pass
   else:
         messagebox.showerror(title="Jingle Music Player", message="There is nothing being currently played!")
def pause(event):
   play_pause()

global dock
dock=False

def start(event):



  try:

    global check
    global don
    don=True


    pygame.mixer.music.stop()
    global dock
    global round
    global sound
    global music
    sound=playlist.curselection()
    music=playlist.get(sound)
    rect = os.path.basename(music)

    var.set("Loaded   -   " + rect)
    check = False

    play.config(image=j)
    pau.config(text="PAUSE")
    pau.place(x=632, y=210)


    round = MP3(music)
    round = round.info.length

    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    timechange()

    dock=True
    mont()









  except:
   pass






def cont():
    global sound
    global round
    global don
    global check
    global main
    global x


    global check


    try:

      py = pygame.mixer.music.get_pos()
      if py == -1:
            sound = playlist.curselection()
            usic = sound[0] + 1



            music = playlist.get(usic)
            rect = os.path.basename(music)
            var.set("Loaded   -   " + rect)
            round = MP3(music)
            round = round.info.length

            pygame.mixer.music.load(music)
            pygame.mixer.music.play()
            check = False
            don == True
            play.config(image=j)
            pau.config(text="PAUSE")
            pau.place(x=632, y=210)
            playlist.selection_clear(0, 'end')
            playlist.activate(usic)
            playlist.selection_set(usic, last=None)
            timechange()



      else:
          pass

    except:
       var.set("The Playlist Finished")
       timechange()





def mont():
  global dock
  try:
   if dock==True:

     x=0
     while x<1:
        cont()
        x=x+1

   elif dock == False :
       var.set("Choose something to play")

   root.after(1000, mont)

  except:
      pass




def stop1(event):
   sto()



def sto():
    global dock

    dock=False
    mont()
    pygame.mixer.music.stop()

    var.set("Choose something to play")
    try:
      timechange()
    except:
        pass

vk = bk.Label(root, font=("Arial Black", 8), text=("TRACK VOLUME = 100"))
vk.place(x=715, y=95)






def timechange():
 global hem
 global gem
 global men
 global sound
 global round
 global music
 global main

 hem = pygame.mixer.music.get_pos()
 men = int(hem / 1000)
 check_time = tt.strftime('%H:%M:%S', tt.gmtime(men))
 main = tt.strftime('%H:%M:%S', tt.gmtime(round))

 james=Entry.get()
 if james=="The Playlist Finished":
     time.config(text="Elapsed Time - 00:00:00 of 00:00:00")

 elif james=="Choose something to play":
     time.config(text="Elapsed Time - 00:00:00 of 00:00:00")


 else:

  try:


         time.config(text="Elapsed Time - " + check_time + " of " + main)
  except:
        time.config(text="Elapsed Time - 00:00:00 of 00:00:00")

  root.after(1000,timechange)



pygame.mixer.music.set_volume(1)
global muted
muted=False


global ram
ram=str(100)


def plus():
    global ram
    global volu
    global muted
    ram=int(ram)+5
    if ram>=100:
        ram=100
        volu = ram / 100
        pygame.mixer.music.set_volume(volu)
        ram = str(ram)

        vk.config(text="TRACK VOLUME = " + ram)
        vk.place(x=715, y=95)
        mau.config(text="MUTE")
        mau.place(x=565, y=325)
        mute.config(image=g)

        muted = False
    else:
     volu=ram/100
     pygame.mixer.music.set_volume(volu)
     ram=str(ram)

     vk.config(text="TRACK VOLUME = "+ ram)
     vk.place(x=715, y=95)
     mau.config(text="MUTE")
     mau.place(x=565, y=325)
     mute.config(image=g)

     muted = False


def plus1(event):
    plus()

def minus():
    global ram
    global volu
    global muted
    ram = int(ram) - 5
    if ram <= 0:
        ram = 0
        volu = ram / 100
        pygame.mixer.music.set_volume(volu)
        ram = str(ram)
        vk.config(text="TRACK VOLUME = " + ram)
        vk.place(x=715, y=95)
        mau.config(text="MUTE")
        mau.place(x=565, y=325)
        mute.config(image=g)

        muted = False
    else:

     volu = ram / 100
     pygame.mixer.music.set_volume(volu)
     ram=str(ram)
     vk.config(text="TRACK VOLUME = " + ram)
     vk.place(x=715, y=95)
     mau.config(text="MUTE")
     mau.place(x=565, y=325)
     mute.config(image=g)

     muted = False


def minus1(event):
    minus()
def p():
    global muted
    global ram
    pygame.mixer.music.set_volume(0)
    mau.config(text="UNMUTE")
    mau.place(x=557,y=325)
    mute.config(image=t)
    vk.config(text="(MUTED)")
    vk.place(x=755,y=95)
    muted=True




def q():
    global muted
    global ram
    ram=int(ram)
    volu = ram / 100
    pygame.mixer.music.set_volume(volu)
    ram = str(ram)

    vk.config(text="TRACK VOLUME = " + ram)
    vk.place(x=715, y=95)

    mau.config(text="MUTE")
    mau.place(x=565, y=325)
    mute.config(image=g)

    muted = False


def mu():
    global muted
    if muted==False:
        p()
    elif muted==True:
        q()





def mu1(event):
    mu()
    


def shuffle():
 
  global check
  global don
  ton = playlist.size()
  

  if ton>0:

   don=True


   t=playlist.size()
   m=int(t)
   q=m-1
   p = rr.randint(0,q)
   check = False

   play.config(image=j)
   pau.config(text="PAUSE")
   pau.place(x=632, y=210)

   pygame.mixer.music.stop()
   playlist.selection_clear(0, 'end')
   playlist.activate(p)
   playlist.selection_set(p, last=None)
   global dock
   global round
   global sound
   sound = playlist.curselection()
   music = playlist.get(sound)
   rect = os.path.basename(music)
   var.set("Loaded   -   " + rect)
   round = MP3(music)
   round = round.info.length

   pygame.mixer.music.load(music)
   pygame.mixer.music.play()
   timechange()

   dock = True
   mont()


  elif ton==0:
      messagebox.showerror(title="Jingle Music Player", message="The playlist is empty.", parent=root)


def shuffle1(event):
    shuffle()

def rewind():
      global check
      global don


      if don==True:
        playlist.selection_clear(0, 'end')
        playlist.activate(0)
        playlist.selection_set(0, last=None)
        check = False
        pygame.mixer.music.stop()
        play.config(image=j)
        pau.config(text="PAUSE")
        pau.place(x=632, y=210)

        global dock
        global round
        global sound
        sound = playlist.curselection()
        music = playlist.get(sound)
        rect = os.path.basename(music)
        var.set("Loaded   -   " + rect)
        round = MP3(music)
        round = round.info.length

        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        timechange()

        dock = True
        mont()

      elif don==False:
          messagebox.showerror(title="Jingle Music Player", message="Either the playlist is empty or hasn't been played yet.", parent=root)

def rewind1(event):
    rewind()


def next():
   global check
   global don
   global dock
   global round
   try:
    if don == True:
        sound=playlist.curselection()
        usic=sound[0]+1

        playlist.selection_clear(0, 'end')
        playlist.activate(usic)
        playlist.selection_set(usic, last=None)
        check = False
        pygame.mixer.music.stop()
        play.config(image=j)
        pau.config(text="PAUSE")
        pau.place(x=632, y=210)


        sound = playlist.curselection()
        music = playlist.get(sound)
        rect = os.path.basename(music)
        var.set("Loaded   -   " + rect)
        round = MP3(music)
        round = round.info.length

        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        timechange()

        dock = True
        mont()
    elif don == False:
        messagebox.showerror(title="Jingle Music Player",
                             message="Either the playlist is empty or hasn't been played yet.", parent=root)
   except:
       playlist.selection_clear(0, 'end')
       playlist.activate('end')
       playlist.selection_set('end', None)
       check = False
       pygame.mixer.music.stop()
       play.config(image=j)
       pau.config(text="PAUSE")
       pau.place(x=632, y=210)



       sound = playlist.curselection()
       music = playlist.get(sound)
       rect = os.path.basename(music)
       var.set("Loaded   -   " + rect)
       round = MP3(music)
       round = round.info.length

       pygame.mixer.music.load(music)
       pygame.mixer.music.play()
       timechange()

       dock = True
       mont()


def next1(event):
    next()

def previous():
   global check
   global don
   global dock
   global round
   try:
    if don == True:
        sound=playlist.curselection()

        usic=sound[0]-1

        playlist.selection_clear(0, 'end')
        playlist.activate(usic)
        playlist.selection_set(usic, last=None)
        check = False
        pygame.mixer.music.stop()
        play.config(image=j)
        pau.config(text="PAUSE")
        pau.place(x=632, y=210)


        sound = playlist.curselection()
        music = playlist.get(sound)
        rect = os.path.basename(music)
        var.set("Loaded   -   " + rect)
        round = MP3(music)
        round = round.info.length

        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        timechange()

        dock = True
        mont()
    elif don == False:
        messagebox.showerror(title="Jingle Music Player",
                             message="Either the playlist is empty or hasn't been played yet.", parent=root)
   except:
       playlist.selection_clear(0, 'end')
       playlist.activate(0)
       playlist.selection_set(0, None)
       check = False
       pygame.mixer.music.stop()
       play.config(image=j)
       pau.config(text="PAUSE")
       pau.place(x=632, y=210)

       sound = playlist.curselection()
       music = playlist.get(sound)
       rect = os.path.basename(music)
       var.set("Loaded   -   " + rect)
       round = MP3(music)
       round = round.info.length

       pygame.mixer.music.load(music)
       pygame.mixer.music.play()
       timechange()

       dock = True
       mont()




def previous1(event):
    previous()


def message():
    messagebox.showinfo(title="Jingle Music Player", message="Jingle Music Player is a mp3 player developed by Pratham Khanduja using python.", parent=root)


def play_mess():
    messagebox.showinfo(title="Jingle Music Player", message="Just click and select a music in the playlist to play it. You can even move up and down the playlist to change it.", parent=root)


def pal():
    messagebox.showinfo(title="Jingle Music Player", message="Use the 'BACKSPACE' key to pause/unpause.", parent=root)

def rel():
    messagebox.showinfo(title="Jingle Music Player", message="Use the 'R' key to reload the playlist. ", parent=root)

def stud():
    messagebox.showinfo(title="Jingle Music Player", message="Use the 'SPACEBAR' to stop music.", parent=root)

def shuff():
    messagebox.showinfo(title="Jingle Music Player", message="Use the 'S' key to shuffle.", parent=root)

def pre():
    messagebox.showinfo(title="Jingle Music Player", message="Use the 'F' key to play the previous track. ", parent=root)

def ne():
    messagebox.showinfo(title="Jingle Music Player", message="Use the 'J' key to play the next track. ", parent=root)

def m():
    messagebox.showinfo(title="Jingle Music Player", message="Use the 'M' key to mute/unmute ", parent=root)

def inc():
    messagebox.showinfo(title="Jingle Music Player", message="Use the '+' key to increase the track volume ", parent=root)

def dec():
    messagebox.showinfo(title="Jingle Music Player", message="Use the '-' key to decrease the track volume ", parent=root)
#ui__________________________________________________________________________________________________________________________________________________________________________________


a=bk.PhotoImage(file="assets\mbox.png")
b=bk.PhotoImage(file="assets\mash.png")
c= bk.PhotoImage(file="assets\play (2).png")
d=bk.PhotoImage(file="assets\ext.png")
e=bk.PhotoImage(file="assets\mack.png")
f=bk.PhotoImage(file="assets\stop.png")
g=bk.PhotoImage(file="assets\mute (2).png")
h=bk.PhotoImage(file="assets\ewind.png")
i=bk.PhotoImage(file="assets\shuffle.png")
j = bk.PhotoImage(file="assets\pause (2).png")
t = bk.PhotoImage(file="assets\sute.png")

v = bk.PhotoImage(file="assets\gash.png")


var=bk.StringVar()

title= bk.Label(root, image=a)
title.place(x=320,y=0)

title1=bk.Label(root, text="Jingle Music Player", font=("Arial Black", 20))
title1.place(x=400,y=0)

playlist_label=bk.Label(root, text="PLAYLIST", font=("Arial Black", 10))
playlist_label.place(x=100, y=60)

playlist=bk.Listbox(root, width='50',height="20")
playlist.place(x=0,y=80)

play=ttk.Button(root, image=j, takefocus=False,  command=play_pause)
play.place(x=620, y=140)
n = ttk.Button(root, image=d, takefocus=False, command=next)
n.place(x=760, y=140)

previo=ttk.Button(root, image=e, takefocus=False, command=previous)
previo.place(x=340, y=140)



stop = ttk.Button(root, image=f, takefocus=False, command=sto)
stop.place(x=480,y=140)


mute = ttk.Button(root, image=g, takefocus=False, command=mu)
mute.place(x=550,y=255)

repeat=ttk.Button(root, image=h, takefocus=False, command=rewind)
repeat.place(x=690, y=255)

random = ttk.Button(root, image=i, takefocus=False, command=shuffle)
random.place(x=410,y=255)

plu = ttk.Button(root, takefocus=False, command=plus, image=jk)
plu.place(x=730, y=55)

mi = ttk.Button(root, takefocus=False, command=minus, image=bl)
mi.place(x=800, y=55)


time = bk.Label(root, text="Elapsed Time   -   00:00:00 of 00:00:00", font=("Arial Black", 10))
time.place(x=460, y=378)

Entry=bk.Entry(root,  state="disabled",cursor="arrow", fg="white",font=("Arial Black", 12),textvariable=var, width=52,)
Entry.pack(side="bottom", fill='x')

var.set("Choose something to play")

prev = bk.Label(root , text="PREVIOUS", font=("Arial Black", 8))
prev.place(x=342, y=210)

st = bk.Label(root , text="STOP", font=("Arial Black", 8))
st.place(x=495, y=210)

pau = bk.Label(root , text="PAUSE", font=("Arial Black", 8))
pau.place(x=632, y=210)

nex = bk.Label(root , text="NEXT", font=("Arial Black", 8))
nex.place(x=775, y=210)

shu = bk.Label(root , text="SHUFFLE", font=("Arial Black", 8))
shu.place(x=415, y=325)

re = bk.Label(root , text="RELOAD", font=("Arial Black", 8))
re.place(x=697, y=325)

mau = bk.Label(root , text="MUTE", font=("Arial Black", 8))
mau.place(x=565, y=325)

playlist.bind('<<ListboxSelect>>', start)


root.bind("<BackSpace>", pause)

root.bind("r", rewind1)

root.bind("<space>", stop1)


root.bind("s", shuffle1)
root.bind("f", previous1)
root.bind("j", next1)
root.bind("m", mu1)
root.bind("+", plus1)
root.bind("=", plus1)
root.bind("-", minus1)
root.bind("_", minus1)



main=bk.Menu(root)

root.config(menu=main)

options=bk.Menu(main)

tutorial=bk.Menu(main)

main.add_cascade(menu=options, label="File")
options.add_command(label="Add to playlist", command=add)
options.add_command(label="Clear playlist", command=delete)
options.add_command(label="Minimize", command=minimize)
options.add_cascade(label="Exit", command=exit2)
main.add_cascade(menu=tutorial, label="Bindings")
main.add_command(label="About", command=message)

tutorial.add_command(label="Play Music", command=play_mess)
tutorial.add_command(label="Pause/Unpause Music", command=pal)
tutorial.add_command(label="Reload Playlist", command=rel)
tutorial.add_command(label="Stop Music", command=stud)
tutorial.add_command(label="Shuffle", command=shuff)
tutorial.add_command(label="Previous Track", command=pre)
tutorial.add_command(label="Next Track", command=ne)
tutorial.add_command(label="Mute/Unmute", command=m)
tutorial.add_command(label="Increase Volume", command=inc)
tutorial.add_command(label="Decrease Volume", command=dec)

pygame.mixer.music.load("assets\Tech.ogg")
pygame.mixer.music.play()













root.mainloop()