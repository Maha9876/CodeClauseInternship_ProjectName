from tkinter import *
import pygame
from tkinter import filedialog
root=Tk()
root.title('Music')
root.geometry("500x400")
pygame.mixer.init()

def add_song():
    song=filedialog.askopenfilename(initialdir='songs',title="choose a song",filetypes=(("mp3 files","*.mp3"),))
    song_box.insert(END,song)
    
def play():
    song=song_box.get(ACTIVE)
    song=song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()
    
song_box=Listbox(root,bg="black",fg="green",width=60)
song_box.pack(pady=20)
    
my_button=Button(root,text="play song",font=("Helvetica",32),bg='green',fg='white',command=play)
my_button.pack(pady=10)
stop_button=Button(root,text="stop",font=("Helvetica",32),bg='red',fg='white',command=stop)
stop_button.pack(pady=20)

my_menu=Menu(root)
root.config(menu=my_menu)

add_song_menu=Menu(my_menu,bg="yellow")
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
add_song_menu.add_command(label="Add One song To Playlist",command=add_song)

root.mainloop()