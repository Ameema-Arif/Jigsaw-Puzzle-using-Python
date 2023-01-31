import pygame as p
import time
from tkinter import *
import sys




class Puzzle(object):

    Sound=r"D:\OOP\Project\SubMusic.ogg"

    def Win(self):
        p.init()
        Wint=p.display.set_mode((400,400))
        p.display.set_caption("Game Over")
        Wimg=p.image.load(r"D:\OOP\Project\game-result-win.png").convert()
        Wimg=p.transform.scale(Wimg,(400,400))
        Wint.blit(Wimg,[10,10])
        p.display.update()
        time.sleep(2)
        
               

    def Lose(self):
        p.init()
        Lint=p.display.set_mode((400,400))
        p.display.set_caption("Game Over")
        Limg=p.image.load(r"D:\OOP\Project\you-lose1.png").convert()
        Limg=p.transform.scale(Limg,(400,400))
        Lint.blit(Limg,[10,10])
        p.display.update()
        time.sleep(1)
        
             

    
    def Sound(self):
       
        p.mixer.init()
        p.mixer.music.load("D:\OOP\Project\SubMusic.ogg")
        p.mixer.music.play()

    

class Easy(Puzzle):

    x=p.init()
    screen=p.display.set_mode((500,400))
    z=p.display.set_caption("Jigsaw puzzle")
    Puzzle.Sound(X)



    first=p.image.load(r"D:\OOP\Project\looneytunes1.png").convert()
    second=p.image.load(r"D:\OOP\Project\looneytunes2.png").convert()
    third=p.image.load(r"D:\OOP\Project\looneytunes3.png").convert()
    fourth=p.image.load(r"D:\OOP\Project\looneytunes4.png").convert()

    first=p.transform.scale(first,(150,150))
    second=p.transform.scale(second,(150,150))
    third=p.transform.scale(third,(150,150))
    fourth=p.transform.scale(fourth,(150,150))



    p.mouse.set_visible(True)
    done=False


    a,b=0,0
    c,d=152,0
    e,f=0,152
    g,h=152,152
    L=[]
    m=[]


    def Win(self):
        Puzzle.Win(self)

    def Lose(self):
        Puzzle.Lose(self)

    
    
    for event in p.event.get():      
            
            screen.blit(first,[a,b])
            screen.blit(second,[c,d])
                            
            screen.blit(third,[e,f])
            screen.blit(fourth,[g,h])

#*********************************Game loop**************************************************************************************************
       
    while done==False:
        
      

        for event in p.event.get():

            screen.blit(fourth,[a,b])
            screen.blit(third,[c,d])
                   
            screen.blit(second,[e,f])
            screen.blit(first,[g,h])
            
            mx,my=p.mouse.get_pos()
            
            #First
            if event.type==p.MOUSEBUTTONDOWN and event.button==1:
                if mx<=150 and 0<= my <=150:
                    L.append([150,0,150])
                    
            #second        
            if event.type==p.MOUSEBUTTONDOWN and event.button==1:
                if 152<= mx <=302 and my<=150:
                    L.append([152,302,150])
                    
            #Third
            if event.type==p.MOUSEBUTTONDOWN and event.button==1:
                if  mx <=152 and 152<= my<=302:
                    L.append([152,152,302])
                    
            #Fourth
            if event.type==p.MOUSEBUTTONDOWN and event.button==1:
                if 152<= mx <=302 and 152<= my<=302:
                    L.append([152,302,152,302])
                    

    #   *********************************************************First**************************************************************************
            #T1->T2
            if len(L)==2 and L[0]==([150,0,150]) and L[1]==([152,302,150]):
                print("X")
                if a==0 and b==0 and c==152 and d==0:
                    a=152
                    c=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)
                    
            #T2->T3
            if len(L)==2 and L[0]==([152,302,150]) and L[1]==([152,152,302]):
                print("X")
                if a==152 and b==0 and e==0 and f==152:
                    a=0
                    b=152
                    e=152
                    f=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T3->T2
            if len(L)==2 and L[1]==([152,302,150]) and L[0]==([152,152,302]):
                print("X")
                if a==0 and b==152 and e==152 and f==0:
                    a=152
                    b=0
                    e=0
                    f=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T2->T4
            if len(L)==2 and L[0]==([152,302,150]) and L[1]==([152,302,152,302]):
                print("X")
                if a==152 and b==0 and g==152 and h==152:
                    b=152
                    h=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T4->T2
            if len(L)==2 and L[1]==([152,302,150]) and L[0]==([152,302,152,302]):
                print("X")
                if a==152 and b==152 and g==152 and h==0:
                    b=0
                    h=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


            #T2->T1
            if len(L)==2 and L[1]==([150,0,150]) and L[0]==([152,302,150]):
                print("X")
                if a==152 and b==0 and c==0 and d==0:
                    a=0
                    b=0
                    c=152
                    d=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T1->T3
            if len(L)==2 and L[0]==([150,0,150]) and L[1]==([152,152,302]):
                print("X")
                if a==0 and b==0 and e==0 and f==152:
                    b=152
                    f=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T3->T2
            if len(L)==2 and L[1]==([152,302,150]) and L[0]==([152,152,302]):
                print("X")
                if a==0 and b==152 and c==152 and d==0:
                    a=152
                    b=0
                    c=0
                    d=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)
                    
            #T2>T3
            if len(L)==2 and L[0]==([152,302,150]) and L[1]==([152,152,302]):
                print("X")
                if a==152 and b==0 and c==0 and d==152:
                    a=0
                    b=152
                    c=152
                    d=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T3->T4
            if len(L)==2 and L[1]==([152,302,152,302]) and L[0]==([152,152,302]):
                print("X")
                if a==0 and b==152 and g==152 and h==152:
                    a=152
                    g=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T4->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([152,302,152,302]):
                print("X")
                if a==152 and b==152 and g==0 and h==152:
                    a=0
                    g=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)
            
            #T3->T1
            if len(L)==2 and L[1]==([150,0,150]) and L[0]==([152,152,302]):
                print("X")
                if a==0 and b==152 and e==0 and f==0:
                    print(8)
                    b=0
                    f=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T1->T4
            if len(L)==2 and L[0]==([150,0,150]) and L[1]==([152,302,152,302]):
                print("X")
                if a==0 and b==0 and g==152 and h==152:
                    a=152
                    b=152
                    g=0
                    h=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T4->T1
            if len(L)==2 and L[1]==([150,0,150]) and L[0]==([152,302,152,302]):
                print("X")
                if a==152 and b==152 and g==0 and h==0:
                    a=0
                    b=0
                    g=152
                    h=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T4->T2
            if len(L)==2 and L[1]==([152,302,150]) and L[0]==([152,302,152,302]):
                print("X")
                if a==152 and b==152 and c==152 and d==0:
                    b=0
                    d=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T2->T4
            if len(L)==2 and L[0]==([152,302,150]) and L[1]==([152,302,152,302]):
                print("X")
                if a==152 and b==0 and c==152 and d==152:
                    d=0
                    b=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


            #T4->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([152,302,152,302]):
                print("X")
                if a==152 and b==152 and e==0 and f==152:
                    a=0
                    e=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T3->T4
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([152,302,152,302]):
                print("X")
                if a==0 and b==152 and e==152 and f==152:
                    e=0
                    a=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

                    
    #         ****************************************************Second************************************************************************
            #T2->T1
            if len(L)==2 and L[0]==([152,302,150]) and L[1]==([150,0,150]):
                print("X")
                if a==0 and b==0 and c==152 and d==0:
                    a=152
                    c=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


            #T1->T2
            if len(L)==2 and L[1]==([152,302,150]) and L[0]==([150,0,150]):
                print("X")
                if a==152 and b==0 and c==0 and d==0:
                    a=0
                    c=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T1->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([150,0,150]):
                print("X")
                if e==0 and f==152 and c==0 and d==0:
                    f=0
                    d=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T3->T1
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([150,0,150]):
                print("X")
                if e==0 and f==0 and c==0 and d==152:
                    d=0
                    f=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

                    
            #T1->T4
            if len(L)==2 and L[1]==([152,302,152,302]) and L[0]==([150,0,150]):
                print("X")
                if g==152 and h==152 and c==0 and d==0:
                    g=0
                    h=0
                    c=152
                    d=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)
                    
            #T4->T1
            if len(L)==2 and L[0]==([152,302,152,302]) and L[1]==([150,0,150]):
                print("X")
                if g==0 and h==0 and c==152 and d==152:
                    c=0
                    d=0
                    g=152
                    h=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            
            #T2->T3
            if len(L)==2 and L[0]==([152,302,150]) and L[1]==([152,152,302]):
                print("X")
                if c==152 and d==0 and e==0 and f==152:
                    c=0
                    d=152
                    e=152
                    f=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            
            #T3->T2
            if len(L)==2 and L[1]==([152,302,150]) and L[0]==([152,152,302]):
                print("X")
                if c==0 and d==152 and e==152 and f==0:
                    c=152
                    d=0
                    e=0
                    f=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T3->T1
            if len(L)==2 and L[1]==([150,0,150]) and L[0]==([152,152,302]):
                print("X")
                if c==0 and d==152 and a==0 and b==0:
                    d=0
                    b=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T1->T3
            if len(L)==2 and L[0]==([150,0,150]) and L[1]==([152,152,302]):
                print("X")
                if c==0 and d==0 and a==0 and b==152:
                    b=0
                    d=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


            #T3->T4
            if len(L)==2 and L[1]==([152,302,152,302]) and L[0]==([152,152,302]):
                print("X")
                if c==0 and d==152 and g==152 and h==152:
                    g=0
                    c=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T4->T3
            if len(L)==2 and L[0]==([152,302,152,302]) and L[1]==([152,152,302]):
                print("X")
                if c==152 and d==152 and g==0 and h==152:
                    c=0
                    g=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


            #T2->T4
            if len(L)==2 and L[0]==([152,302,150]) and L[1]==([152,302,152,302]):
                print("X")
                if c==152 and d==0 and g==152 and h==152:
                    d=152
                    h=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T4->T2
            if len(L)==2 and L[1]==([152,302,150]) and L[0]==([152,302,152,302]):
                print("X")
                if c==152 and d==152 and g==152 and h==0:
                    d=0
                    h=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T4->T1
            if len(L)==2 and L[1]==([150,0,150]) and L[0]==([152,302,152,302]):
                print("X")
                if c==152 and d==152 and a==0 and b==0:
                    c=0
                    d=0
                    a=152
                    b=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)
                    
            #T1->T4
            if len(L)==2 and L[0]==([150,0,150]) and L[1]==([152,302,152,302]):
                print("X")
                if a==152 and b==152 and c==0 and d==0:
                    a=0
                    b=0
                    c=152
                    d=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

                    
            #T4->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([152,302,152,302]):
                print("X")
                if c==152 and d==152 and e==0 and f==152:
                    c=0
                    e=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T3->T4
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([152,302,152,302]):
                print("X")
                if c==0 and d==152 and e==152 and f==152:
                    e=0
                    c=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


    #     *******************************************************Third*****************************************************************************
            #T3->T1
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([150,0,150]):
                print("X")
                if a==0 and b==0 and e==0 and f==152:
                    b=152
                    f=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T1->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([150,0,150]):
                print("X")
                if a==0 and b==152 and e==0 and f==0:
                    b=0
                    f=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T1->T2
            if len(L)==2 and L[1]==([152,302,150]) and L[0]==([150,0,150]):
                print("X")
                if e==0 and f==0 and c==152 and d==0:
                    e=152
                    c=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T2->T1
            if len(L)==2 and L[0]==([152,302,150]) and L[1]==([150,0,150]):
                print("X")
                if e==152 and f==0 and c==0 and d==0:
                    e=0
                    c=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


            #T1->T4
            if len(L)==2 and L[1]==([152,302,152,302]) and L[0]==([150,0,150]):
                print("X")
                if g==152 and h==152 and e==0 and f==0:
                    g=0
                    h=0
                    e=152
                    f=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T4->T1
            if len(L)==2 and L[0]==([152,302,152,302]) and L[1]==([150,0,150]):
                print("X")
                if e==152 and f==152 and g==0 and h==0:
                    e=0
                    f=0
                    g=152
                    h=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            
            #T3->T2
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([152,302,150]):
                print("X")
                if c==152 and d==0 and e==0 and f==152:
                    c=0
                    d=152
                    e=152
                    f=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            
            #T2->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([152,302,150]):
                print("X")
                if c==0 and d==152 and e==152 and f==0:
                    c=152
                    d=0
                    e=0
                    f=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)
            #T2->T1
            if len(L)==2 and L[1]==([152,0,150]) and L[0]==([152,302,150]):
                print("X")
                if a==0 and b==0 and e==152 and f==0:
                    a=152
                    e=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)
                    
            #T1->T2
            if len(L)==2 and L[0]==([152,0,150]) and L[1]==([152,302,150]):
                print("X")
                if a==152 and b==0 and e==0 and f==0:
                    a=0
                    e=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            
            #T2->T4
            if len(L)==2 and L[1]==([152,302,152,302]) and L[0]==([152,302,150]):
                print("X")
                if e==152 and f==0 and g==152 and h==152:
                    f=152
                    h=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T4->T2
            if len(L)==2 and L[0]==([152,302,152,302]) and L[1]==([152,302,150]):
                print("X")
                if e==152 and f==152 and g==152 and h==0:
                    f=0
                    h=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


            #T3->T4
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([152,302,152,302]):
                print("X")
                if e==0 and f==152 and g==152 and h==152:
                    e=152
                    g=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T4->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([152,302,152,302]):
                print("X")
                if e==152 and f==152 and g==0 and h==152:
                    e=0
                    g=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)
            #T4->T1
            if len(L)==2 and L[1]==([150,0,150]) and L[0]==([152,302,152,302]):
                print("X")
                if e==152 and f==152 and a==0 and b==0:
                    e=0
                    f=0
                    a=152
                    b=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T1->T4
            if len(L)==2 and L[0]==([150,0,150]) and L[1]==([152,302,152,302]):
                print("X")
                if a==152 and b==152 and e==0 and f==0:
                    a=0
                    b=0
                    e=152
                    f=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

                    
            #T4->T2
            if len(L)==2 and L[1]==([152,302,150]) and L[0]==([152,302,152,302]):
                print("X")
                if e==152 and f==152 and c==152 and d==0:
                    f=0
                    d=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)
                    
            #T2->T4
            if len(L)==2 and L[0]==([152,302,150]) and L[1]==([152,302,152,302]):
                print("X")
                if e==152 and f==0 and c==152 and d==152:
                    f=152
                    d=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            
    #    **************************************************************Fourth************************************************************************
            
            #T4->T1
            if len(L)==2 and L[0]==([152,302,152,302]) and L[1]==([150,0,150]):
                print("X")
                if a==0 and b==0 and g==152 and h==152:
                    a=152
                    b=152
                    g=0
                    h=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T1->T4
            if len(L)==2 and L[1]==([152,302,152,302]) and L[0]==([150,0,150]):
                print("X")
                if a==152 and b==152 and g==0 and h==0:
                    a=0
                    b=0
                    g=152
                    h=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T1->T2
            if len(L)==2 and L[1]==([152,302,150]) and L[0]==([150,0,150]):
                print("X")
                if c==152 and d==0 and g==0 and h==0:
                    c=0
                    g=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T2->T1
            if len(L)==2 and L[0]==([152,302,150]) and L[1]==([150,0,150]):
                print("X")
                if c==0 and d==0 and g==152 and h==0:
                    c=152
                    g=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


            #T1->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([150,0,150]):
                print("X")
                if e==0 and f==152 and g==0 and h==0:
                    f=0
                    h=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T3->T1
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([150,0,150]):
                print("X")
                if e==0 and f==0 and g==0 and h==152:
                    f=152
                    h=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            
            #T4->T2
            if len(L)==2 and L[0]==([152,302,152,302]) and L[1]==([152,302,150]):
                print("X")
                if c==152 and d==0 and g==152 and h==152:
                    h=0
                    d=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            
            #T2->T4
            if len(L)==2 and L[1]==([152,302,152,302]) and L[0]==([152,302,150]):
                print("X")
                if c==152 and d==152 and g==152 and h==0:
                    d=0
                    h=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T2->T1
            if len(L)==2 and L[1]==([150,0,150]) and L[0]==([152,302,150]):
                print("X")
                if a==0 and b==0 and g==152 and h==0:
                    g=0
                    a=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T1->T2
            if len(L)==2 and L[0]==([150,0,150]) and L[1]==([152,302,150]):
                print("X")
                if a==152 and b==0 and g==0 and h==0:
                    a=0
                    g=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


            #T2->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([152,302,150]):
                print("X")
                if e==0 and f==152 and g==152 and h==0:
                    e=152
                    f=0
                    g=0
                    h=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T3->T2
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([152,302,150]):
                print("X")
                if e==152 and f==0 and g==0 and h==152:
                    e=0
                    f=152
                    g=152
                    h=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


            #T4->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([152,302,152,302]):
                print("X")
                if e==0 and f==152 and g==152 and h==152:
                    e=152
                    g=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T3->T4
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([152,302,152,302]):
                print("X")
                if e==152 and f==152 and g==0 and h==152:
                    e=0
                    g=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)
            #T3->T1
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([150,0,150]):
                print("X")
                if a==0 and b==0 and g==0 and h==152:
                    h=0
                    b=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T1->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([150,0,150]):
                print("X")
                if a==0 and b==152 and g==0 and h==0:
                    b=0
                    h=152
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)


            #T3->T2
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([152,302,150]):
                print("X")
                if c==152 and d==0 and g==0 and h==152:
                    c=0
                    d=152
                    g=152
                    h=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)

            #T2->T3
            if len(L)==2 and L[1]==([152,152,302]) and L[0]==([152,302,150]):
                print("X")
                if c==0 and d==152 and g==152 and h==0:
                    g=0
                    h=152
                    c=152
                    d=0
                    L.remove(L[0])
                    L.remove(L[0])
                    m.append(1)
     
                    
    #    **********************************************************************************************************************************************
            #T1->T1
            if len(L)==2 and L[0]==([150,0,150]) and L[1]==([150,0,150]):
                L.remove(L[0])


            #T2->T2
            if len(L)==2 and L[0]==([152,302,150]) and L[1]==([152,302,150]):
                L.remove(L[0])


            #T3->T3
            if len(L)==2 and L[0]==([152,152,302]) and L[1]==([152,152,302]):
                L.remove(L[0])
        

            #T4->T4
            if len(L)==2 and L[0]==([152,302,152,302]) and L[1]==([152,302,152,302]):
                L.remove(L[0])
        
        
            if len(m)==2 and g==0 and h==0 and e==152 and f==0 and c==0 and d==152 and a==152 and b==152:
                print("")
                
            if event.type==p.QUIT:
                done=True
                if 2<=len(m)<=5:
                    r=Tk()
                    r.title("Score")
                    label=Label(r,text="Your Score is 100")
                    label.grid(row=0,columnspan=8)
                    r.mainloop
                    Win(X)

                if 6<=len(m)<=10:
                    r=Tk()
                    r.title("Score")
                    label=Label(r,text="Your Score is 50")
                    label.grid(row=0,columnspan=8)
                    r.mainloop
                    Win(X)

                if 11<=len(m)<=15:
                    r=Tk()
                    r.title("Score")
                    label=Label(r,text="Your Score is 20")
                    label.grid(row=0,columnspan=8)
                    r.mainloop
                    Win(X)

        

                
            if len(m)>15:
                Lose(X)
            p.display.update()    

      
p.quit()

