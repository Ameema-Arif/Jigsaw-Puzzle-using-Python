from tkinter import *
import pygame as p
import time



class Main(object):
    p.init()
    bg_music="D:\Project\MainMusic.ogg"
    bg_img="D:\Project\puzzle_main.png"
    
    def __init__(self,master):
        self.master = master
        master.title("Jisgaw Puzzle")
        master.configure(bg="black")
        
        
        self.canv = Canvas(master)
        self.img = PhotoImage(file=r"D:\Project\puzzle_main.png")
        self.canv.create_image(0,0, anchor=CENTER, image=self.img)
        self.canv.pack()
        self.music=Main.music(self)

      
        
        self.play= Button(master, text="PLAY", command=self.Play,height=3,width=15)
        self.play.pack()
        
        self.instruction = Button(master, text="INSTRUCTIONS",command=self.Instructions,height=3,width=15)
        self.instruction.pack()

        self.close_button = Button(master, text="EXIT", command=self.Exit,height=3,width=15)
        self.close_button.pack()
   
    def Play(self):
            root.destroy()
            root1=Tk()
            root1.title("Jigsaw Puzzle")
            
            self.canv = Canvas(root1)
            self.img = PhotoImage(file=r"D:\Project\puzzle_main.png")
            self.canv.create_image(0,0, anchor =CENTER, image=self.img)
            self.canv.pack()
            root1.configure(bg="black")
       
            self.easy=Button(root1,text="EASY",command=self.Ease, height=3,width=15).pack()
            self.medium=Button(root1,text="MEDIUM",command=self.Med,height=3,width=15).pack()
            self.hard=Button(root1,text="HARD",command=self.Hard,height=3,width=15).pack()
    
    def music(self):
        p.mixer.init()
        p.mixer.music.load("D:\Project\MainMusic.ogg")
        p.mixer.music.play()
        
    def Ease(self):
        import easy

    def Med(self):
        import medium

    def Hard(self):
        import hard

    def Instructions(self):
        p.init()
        Inst=p.display.set_mode((400,400))
        p.display.set_caption("Instructions")
        Inimg=p.image.load(r"D:\Project\inst.png").convert()
        Inimg=p.transform.scale(Inimg,(350,350))
        Inst.blit(Inimg,[25,25])
        p.display.update()
        time.sleep(2)
        done=False
        while done==False:
        
      

          for event in p.event.get():
            if event.type== p.QUIT:
             done=True
             p.quit()
       

    def Exit(self):
        quit()
        
        
    
root = Tk()
root.title("Jigsaw Puzzle")
my_gui = Main(root)
root.mainloop

