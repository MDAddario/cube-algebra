import random
from tkinter import *

root = Tk()

Up = []
Front = []
Right = []
Back = []
Left = []
Down = []
StickerLabels = []
Section = []
CrossIndex = [0, 0, 0, 0]
Faces = [Up, Front, Right, Back, Left, Down]
scale = 4
printerstate = 1
v = IntVar()
angleindex = 0
numberswitch = 0


'''
#IMPORTANT CUBE CONVENTION FOR THIS SCRIPT
#Clockwise surface arrow arrangement
#Up points Back points Right points Up
#Front points Down points Left points Front
'''


def initialize():
    for y in range(0, 9):
        Up.append("white")
        Front.append("green")
        Right.append("red")
        Back.append("blue")
        Left.append("orange")
        Down.append("yellow")
        StickerLabels.append([])
        for x in range(0, 12):
            StickerLabels[y].append(0)
    for x in range(0, 5):
        Section.append(0)
        Section[x] = Frame(root)
        Section[x].pack()
    Radiobutton(Section[2], text="Clockwise", variable=v, value=1, command=clockwise).pack(anchor=W)
    Radiobutton(Section[2], text="Anti Clockwise", variable=v, value=2, command=anticlockwise).pack(anchor=W)
    Radiobutton(Section[2], text="Half Turn", variable=v, value=3, command=halfturn).pack(anchor=W)
    Button(Section[2], text="R", command=R).pack(side=LEFT)
    Button(Section[2], text="U", command=U).pack(side=LEFT)
    Button(Section[2], text="F", command=F).pack(side=LEFT)
    Button(Section[2], text="D", command=D).pack(side=LEFT)
    Button(Section[2], text="L", command=L).pack(side=LEFT)
    Button(Section[2], text="B", command=B).pack(side=LEFT)
    Button(Section[2], text="Scale Up", command=scaleup).pack(side=LEFT)
    Button(Section[2], text="Scale Down", command=scaledown).pack(side=LEFT)
    Button(Section[2], text="Reset Cube", command=resetcube).pack(side=LEFT)
    Button(Section[2], text="Scramble", command=scramble).pack(side=LEFT)
    Button(Section[2], text="Toggle Numbers", command=numberflip).pack(side=LEFT)
    Button(Section[2], text="Quit", command=root.quit).pack(side=LEFT)
    Button(Section[3], text="Cross", command=cross).pack(side=LEFT)
    Button(Section[3], text="F2L", command=F2L).pack(side=LEFT)
    Button(Section[3], text="OLL", command=OLL).pack(side=LEFT)
    Button(Section[3], text="PLL", command=PLL).pack(side=LEFT)
    Button(Section[4], text="Algorithm Tester", command=testalg).grid(row=0, column=0)
    global algorithmbox
    algorithmbox = Entry(Section[4])
    algorithmbox.insert(10, "RUR'U'")
    algorithmbox.grid(row=0, column=1)
    global results
    results = Label(Section[4])
    results.grid(row=0, column=2)
    clockwise()
    printcube()


def rotation0(face1, face2, face3, face4, face5):
    u = face1[0]
    face1[0] = face1[6]
    face1[6] = face1[8]
    face1[8] = face1[2]
    face1[2] = u
    u = face1[1]
    face1[1] = face1[3]
    face1[3] = face1[7]
    face1[7] = face1[5]
    face1[5] = u
    u = face2[8]
    face2[8] = face3[0]
    face3[0] = face4[2]
    face4[2] = face5[6]
    face5[6] = u
    u = face2[7]
    face2[7] = face3[1]
    face3[1] = face4[5]
    face4[5] = face5[3]
    face5[3] = u
    u = face2[6]
    face2[6] = face3[2]
    face3[2] = face4[8]
    face4[8] = face5[0]
    face5[0] = u
    if printerstate == 1:
        printcube()


def rotation1(face1, face2, face3, face4, face5):
    u = face1[0]
    face1[0] = face1[2]
    face1[2] = face1[8]
    face1[8] = face1[6]
    face1[6] = u
    u = face1[1]
    face1[1] = face1[5]
    face1[5] = face1[7]
    face1[7] = face1[3]
    face1[3] = u
    u = face2[8]
    face2[8] = face5[6]
    face5[6] = face4[2]
    face4[2] = face3[0]
    face3[0] = u
    u = face2[7]
    face2[7] = face5[3]
    face5[3] = face4[5]
    face4[5] = face3[1]
    face3[1] = u
    u = face2[6]
    face2[6] = face5[0]
    face5[0] = face4[8]
    face4[8] = face3[2]
    face3[2] = u
    if printerstate == 1:
        printcube()


def rotation2(face1, face2, face3, face4, face5):
    face1[1], face1[7] = face1[7], face1[1]
    face1[3], face1[5] = face1[5], face1[3]
    face1[0], face1[8] = face1[8], face1[0]
    face1[2], face1[6] = face1[6], face1[2]
    face2[8], face4[2] = face4[2], face2[8]
    face2[7], face4[5] = face4[5], face2[7]
    face2[6], face4[8] = face4[8], face2[6]
    face3[0], face5[6] = face5[6], face3[0]
    face3[1], face5[3] = face5[3], face3[1]
    face3[2], face5[0] = face5[0], face3[2]
    if printerstate == 1:
        printcube()


def U(index=0):
    if index+angleindex == 0:
        rotation0(Up, Front, Right, Back, Left)
    elif index+angleindex == 1:
        rotation1(Up, Front, Right, Back, Left)
    else:
        rotation2(Up, Front, Right, Back, Left)


def R(index=0):
    if index+angleindex == 0:
        rotation0(Right, Down, Back, Up, Front)
    elif index+angleindex == 1:
        rotation1(Right, Down, Back, Up, Front)
    else:
        rotation2(Right, Down, Back, Up, Front)


def F(index=0):
    if index+angleindex == 0:
        rotation0(Front, Up, Left, Down, Right)
    elif index+angleindex == 1:
        rotation1(Front, Up, Left, Down, Right)
    else:
        rotation2(Front, Up, Left, Down, Right)


def B(index=0):
    if index+angleindex == 0:
        rotation0(Back, Left, Up, Right, Down)
    elif index+angleindex == 1:
        rotation1(Back, Left, Up, Right, Down)
    else:
        rotation2(Back, Left, Up, Right, Down)


def L(index=0):
    if index+angleindex == 0:
        rotation0(Left, Back, Down, Front, Up)
    elif index+angleindex == 1:
        rotation1(Left, Back, Down, Front, Up)
    else:
        rotation2(Left, Back, Down, Front, Up)


def D(index=0):
    if index+angleindex == 0:
        rotation0(Down, Right, Front, Left, Back)
    elif index+angleindex == 1:
        rotation1(Down, Right, Front, Left, Back)
    else:
        rotation2(Down, Right, Front, Left, Back)


'''
#Add Inner Slice Moves (M)
#Add Double Layer turns (r)
#Add cube rotations (x,y,z)
'''


def clockwise():
    global angleindex
    angleindex = 0
    Radiobutton(Section[2], text="Clock", variable=v, value=1, command=clockwise).select()


def anticlockwise():
    global angleindex
    angleindex = 1
    Radiobutton(Section[2], text="Anti", variable=v, value=2, command=anticlockwise).select()


def halfturn():
    global angleindex
    angleindex = 2
    Radiobutton(Section[2], text="Double", variable=v, value=3, command=halfturn).select()


def resetcube():
    clockwise()
    for x in range(0, 9):
        Up[x] = "white"
        Front[x] = "green"
        Right[x] = "red"
        Back[x] = "blue"
        Left[x] = "orange"
        Down[x] = "yellow"
    printcube()


def scramble():
    clockwise()
    global printerstate
    printerstate = 0
    k = 20
    previous = 6
    print("Scramble", end=": ", flush=True)
    for x in range(0, k):
        ranface = random.randint(0, 5)
        randeg = random.randint(0, 2)
        if ranface == previous:
            k += 1
            continue
        previous = ranface
        if ranface == 0:
            U(randeg)
            print("U", end="", flush=True)
        elif ranface == 1:
            F(randeg)
            print("F", end="", flush=True)
        elif ranface == 2:
            R(randeg)
            print("R", end="", flush=True)
        elif ranface == 3:
            B(randeg)
            print("B", end="", flush=True)
        elif ranface == 4:
            D(randeg)
            print("D", end="", flush=True)
        else:
            L(randeg)
            print("L", end="", flush=True)
        if randeg == 0:
            print(end=" ", flush=True)
        elif randeg == 1:
            print("'", end=" ", flush=True)
        else:
            print("2", end=" ", flush=True)
    print("")
    printerstate = 1
    printcube()


def scaleup():
    global scale
    if scale < 6:
        scale += 1
        printcube()


def scaledown():
    global scale
    if scale > 1:
        scale -= 1
        printcube()


def testalg():
    global rawalg
    global iteration
    global breaker
    global printerstate
    global results
    rawalg = algorithmbox.get()
    algorithmbox.delete(0, END)
    alg = rawalg + "000"
    lengthalg = len(rawalg)
    results.grid_forget()
    if rawalg == "":
        results = Label(Section[4], text="Please enter an algorithm")
        results.grid(row=0, column=2)
        return
    iteration = 0
    breaker = 0
    printerstate = 0
    resetcube()
    while breaker == 0:
        iteration += 1
        antiiterate = lengthalg
        for w in range(0, lengthalg):
            if alg[w] == "U":
                if alg[w+1] == "\'" or alg[w+1] == "1":
                    U(1)
                elif alg[w+1] == "2":
                    U(2)
                else:
                    U(0)
            elif alg[w] == "R":
                if alg[w+1] == "\'" or alg[w+1] == "1":
                    R(1)
                elif alg[w+1] == "2":
                    R(2)
                else:
                    R(0)
            elif alg[w] == "F":
                if alg[w+1] == "\'" or alg[w+1] == "1":
                    F(1)
                elif alg[w+1] == "2":
                    F(2)
                else:
                    F(0)
            elif alg[w] == "D":
                if alg[w+1] == "\'" or alg[w+1] == "1":
                    D(1)
                elif alg[w+1] == "2":
                    D(2)
                else:
                    D(0)
            elif alg[w] == "B":
                if alg[w+1] == "\'" or alg[w+1] == "1":
                    B(1)
                elif alg[w+1] == "2":
                    B(2)
                else:
                    B(0)
            elif alg[w] == "L":
                if alg[w+1] == "\'" or alg[w+1] == "1":
                    L(1)
                elif alg[w+1] == "2":
                    L(2)
                else:
                    L(0)
            elif alg[w:w+4] == "Sexy" or alg[w:w+4] == "sexy":
                R(0)
                U(0)
                R(1)
                U(1)
            else:
                antiiterate -= 1
        if antiiterate == 0:
            results = Label(Section[4], text= rawalg + ' does not affect the cube!')
            results.grid(row=0, column=2)
            return
        checksolved()
    printerstate = 1
    for w in range(0, lengthalg):
        if alg[w] == "U":
            if alg[w + 1] == "\'" or alg[w + 1] == "1":
                U(1)
            elif alg[w + 1] == "2":
                U(2)
            else:
                U(0)
        elif alg[w] == "R":
            if alg[w + 1] == "\'" or alg[w + 1] == "1":
                R(1)
            elif alg[w + 1] == "2":
                R(2)
            else:
                R(0)
        elif alg[w] == "F":
            if alg[w + 1] == "\'" or alg[w + 1] == "1":
                F(1)
            elif alg[w + 1] == "2":
                F(2)
            else:
                F(0)
        elif alg[w] == "D":
            if alg[w + 1] == "\'" or alg[w + 1] == "1":
                D(1)
            elif alg[w + 1] == "2":
                D(2)
            else:
                D(0)
        elif alg[w] == "B":
            if alg[w + 1] == "\'" or alg[w + 1] == "1":
                B(1)
            elif alg[w + 1] == "2":
                B(2)
            else:
                B(0)
        elif alg[w] == "L":
            if alg[w + 1] == "\'" or alg[w + 1] == "1":
                L(1)
            elif alg[w + 1] == "2":
                L(2)
            else:
                L(0)
        elif alg[w:w + 4] == "Sexy" or alg[w:w + 4] == "sexy":
            R(0)
            U(0)
            R(1)
            U(1)


def checksolved():
    global results
    stickernum = 0
    for k in range(0, 6):
        a = Faces[k][0]
        for i in Faces[k]:
            if i == a:
                stickernum += 1
    if stickernum == 54:
        results = Label(Section[4], text='Solved ' + rawalg + ' in ' + str(iteration) + ' steps!')
        results.grid(row=0, column=2)
        global breaker
        breaker = 1


def printcube():
    for y in range(0, 3):
        for x in range(3, 6):
            stickerprint(y, x)
    for y in range(3, 6):
        for x in range(0, 12):
            stickerprint(y, x)
    for y in range(6, 9):
        for x in range(3, 6):
            stickerprint(y, x)


def stickerprint(rownum, colnum):
    if rownum < 3:
        magic = rownum+3*(2-(colnum-3))
        face = Back
    elif 2 < rownum < 6:
        if colnum < 3:
            magic = 8-(3*(rownum-3)+colnum)
            face = Left
        elif 2 < colnum < 6:
            magic = 3*(rownum-3)+(colnum-3)
            face = Up
        elif 5 < colnum < 9:
            magic = 3*(colnum-6)+(2-(rownum-3))
            face = Right
        else:
            magic = (rownum-3)+3*(2-(colnum-9))
            face = Down
    else:
        magic = 8-(3*(rownum-6)+(colnum-3))
        face = Front
    if numberswitch == 1:
        StickerLabels[rownum][colnum] = Label\
            (Section[1], text=magic, height=scale, width=scale*2, bg=face[magic], borderwidth=2, relief="solid")
    else:
        StickerLabels[rownum][colnum] = Label\
            (Section[1], height=scale, width=scale * 2, bg=face[magic], borderwidth=2, relief="solid")
    StickerLabels[rownum][colnum].grid\
        (row=rownum, column=colnum)


def numberflip():
    global numberswitch
    if numberswitch == 1:
        numberswitch = 0
    else:
        numberswitch = 1
    printcube()


def cross():
    reference = Down[4]
    for x in range(0, 4):
        if Down[int(2*x+1)] == reference:
            CrossIndex[x] = 1
        else:
            CrossIndex[x] = 0
    while Down[1] != reference or Down[3] != reference or Down[5] != reference or Down[7] != reference:
        if Left[5] == reference:
            L(1)
            D()
            F(1)
            D(1)
            CrossIndex[0] = 1
        if Front[1] == reference:
            F(1)
            D()
            R(1)
            D(1)
            CrossIndex[2] = 1
        if Right[7] == reference:
            R(1)
            D()
            B(1)
            D(1)
            CrossIndex[3] = 1
        if Back[3] == reference:
            B(1)
            D()
            L(1)
            D(1)
            CrossIndex[1] = 1
        for x in range(0,4):
            if Up[int(2*x+1)] == reference:
                number = int(-4/3*(x*x*x)+6*(x*x)-17/3*x+1)
                print(number)
                if CrossIndex[number] == 0:
                    if x == 0:
                        B(2)
                    elif x == 1:
                        L(2)
                    elif x == 2:
                        R(2)
                    else:
                        F(2)
        break
    printcube()


def F2L():
    algorithmbox.delete(0, END)
    algorithmbox.insert(10, "F2L not ready")


def OLL():
    algorithmbox.delete(0, END)
    algorithmbox.insert(10, "OLL not ready")


def PLL():
    algorithmbox.delete(0, END)
    algorithmbox.insert(10, "PLL not ready")


initialize()


root.mainloop()
