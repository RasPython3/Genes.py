#!/usr/bin/Python3
import tkinter as tk
from random import randint as ran
import time
from tkinter import filedialog as tkFileDialog
from tkinter import messagebox
import os, sys

#print(sys.argv)

sleep = time.sleep

version = '1.0.0'
old_ver = '1.0.0'
root = tk.Tk(className = " Genes.py-"+version) #self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
path = str(os.getcwd())
dame = []
name = 'test.gnsp'
recode_name = 'test.gnsr'
recoding = 0
hiki = ''
foods = ''
start = False
max = 500
kakuritu = 10
hosyoku = True
eatzatsu = False
esa = []
seibutsu = {}
cnumber = ''
life = ''
cells = ''
ce1 = ''
ce2 = ''
ce3 = ''
ce4 = ''
ce5 = ''
ce6 = ''
ce7 = ''
ce8 = ''
ce9 = ''
ce10 = ''
sample = ''
times = 0
val1 = tk.IntVar()
val1.set(500)
val2 = tk.IntVar()
val2.set(10)
rdb1 = tk.IntVar()
rdb1.set(True)
rdb2 = tk.IntVar()
rdb2.set(False)
bt = tk.IntVar()
bt.set(False)

hatsu = True
high = False
stoped = False
tests = 80
subwin = ''

t_ = time.time()
T_ = 0
fps = 0

def get_temp():
    global start, stoped, high, tests
    with open('/sys/class/thermal/thermal_zone0/temp', mode = 'r') as f:
        temp = f.read()
    temp = int(temp)/10**(len(temp)-3)
    #print(temp)
    #temp = tests
    if temp >= 65 and not high and not stoped:
        high = True
        if start:
            start = False
            stoped = True
        messagebox.showwarning(' CPU温度異常 ', 'CPU温度が65度を超えたため、強制停止しています。')
    elif temp < 55 and high:
        high = False
        if stoped:
            start = True
            stoped = False
            messagebox.showinfo(' CPU温度回復 ', 'CPU温度が回復したため、再開しています。')
        else:
            messagebox.showinfo(' CPU温度回復 ', 'CPU温度が回復しました。')
    elif temp > 55 and high and start:
        start = False
        stoped = True
        messagebox.showerror(' CPU温度異常 ', 'CPU温度はまだ回復していません!!!')
    #tests -= 0.5
    root.after(100, get_temp)

def buttonsta():
    global start
    global hatsu
    global hiki
    global foods
    start = True
    if high:
        return
    if hatsu == True:
        for sen in range(5, 806, 80):
            world.create_line(sen, 5, sen, 805, fill = 'green')
        for sen in range(5, 806, 80):
            world.create_line(5, sen, 805, sen, fill = 'green')
        global seibutsu
        for jun in range(1,11):
            seibutsu[jun] = [1, 0x1fff, 405, 405, 0xD0, world.create_oval(405-2, 405-2, 405+2, 405+2, tags = str(jun), outline = '#ff3f3f', fill = '#000000')]
            world.tag_bind(seibutsu[jun][5], '<Button-1>', click)
        #seibutsu[11] = [10, 0x9ffa, 405, 405, 0xd0, world.create_oval(405-2, 405-2, 405+2, 405+2, outline = '#ff0000', fill = '#000000'), 405, 405, 0xd0, world.create_oval(405-2, 405-2, 405+2, 405+2, outline = '#ff0000', fill = '#000000'), 405, 405, 0xd0, world.create_oval(405-2, 405-2, 405+2, 405+2, outline = '#ff0000', fill = '#000000'), 405, 405, 0xd0, world.create_oval(405-2, 405-2, 405+2, 405+2, outline = '#ff0000', fill = '#000000'), 405, 405, 0xd0, world.create_oval(405-2, 405-2, 405+2, 405+2, outline = '#ff0000', fill = '#000000'), 405, 405, 0xd0, world.create_oval(405-2, 405-2, 405+2, 405+2, outline = '#ff0000', fill = '#000000'), 405, 405, 0xd0, world.create_oval(405-2, 405-2, 405+2, 405+2, outline = '#ff0000', fill = '#000000'), 405, 405, 0xd0, world.create_oval(405-2, 405-2, 405+2, 405+2, outline = '#ff0000', fill = '#000000'), 405, 405, 0xd0, world.create_oval(405-2, 405-2, 405+2, 405+2, outline = '#ff0000', fill = '#000000'), 405, 405, 0xd0, world.create_oval(405-2, 405-2, 405+2, 405+2, outline = '#ff0000', fill = '#000000')]
        hiki = 10
        foods = 0
        world.itemconfig(echo1, window = plives.config(text = str(hiki)))
        world.itemconfig(echo2, window = pfoods.config(text = str(foods)))
        hatsu = False
        move()

def buttonsto():
    global start, stoped
    start = False
    stoped = False

def scl1(foodmax):
    global max
    global fm
    max = int(foodmax)
    world.itemconfig(fm, window = scale1.config(label = 'FoodsMAX: '+foodmax))#, orient = 'h', from_ = 500, to = 4100, showvalue = False, variable = val1, length = 140, sliderlength = 15, resolution = 1, bg = 'gray', command = scl1))

def scl2(pa):
    global kakuritu
    kakuritu = int(pa)
    world.itemconfig(ka, window = scale2.config(label = 'Mutation(1/n): '+pa))

def caneat():
    global hosyoku
    hosyoku = not hosyoku
    rdb1.set(hosyoku)

def eatall():
    global eatzatsu
    eatzatsu = not eatzatsu
    rdb2.set(eatzatsu)


def click(ev):
    print('1')
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global c9
    global c10
    global sample
    #print(ev)
    ev = str(world.itemcget(world.find_closest(ev.x, ev.y), 'tags')).replace(' ', '').replace('current', '')
    #print(ev)
    if len(ev) == 0:
        return
    ev2 = ev
    for ints in range(10):
        ev2 = ev2.replace(str(ints), '')
        #print([str(ints), ev2])
    #print(ev2)
    if len(ev2) > 0:
        return
    #print('passed')
    ev = int(ev)
    cell = seibutsu[ev][0]
    world.itemconfig(c1, window = cp1.config(text = str(ev)))
    world.itemconfig(c2, window = cp2.config(text = str(int(seibutsu[ev][1]))))
    world.itemconfig(c3, window = cp3.config(text = str(seibutsu[ev][0])))
    world.itemconfig(c4, window = cp4.config(text = '%02X' % seibutsu[ev][4]))
    world.itemconfig(c5, window = cp5.config(text = '%02X' % seibutsu[ev][8*(seibutsu[ev][0] >= 2)]*(seibutsu[ev][0] >= 2)))
    world.itemconfig(c6, window = cp6.config(text = '%02X' % seibutsu[ev][12*(seibutsu[ev][0] >= 3)]*(seibutsu[ev][0] >= 3)))
    world.itemconfig(c7, window = cp7.config(text = '%02X' % seibutsu[ev][16*(seibutsu[ev][0] >= 4)]*(seibutsu[ev][0] >= 4)))
    world.itemconfig(c8, window = cp8.config(text = '%02X' % seibutsu[ev][20*(seibutsu[ev][0] >= 5)]*(seibutsu[ev][0] >= 5)))
    world.itemconfig(c9, window = cp9.config(text = '%02X' % seibutsu[ev][24*(seibutsu[ev][0] >= 6)]*(seibutsu[ev][0] >= 6)))
    world.itemconfig(c10, window = cp10.config(text = '%02X' % seibutsu[ev][28*(seibutsu[ev][0] >= 7)]*(seibutsu[ev][0] >= 7)))
    world.itemconfig(c11, window = cp11.config(text = '%02X' % seibutsu[ev][32*(seibutsu[ev][0] >= 8)]*(seibutsu[ev][0] >= 8)))
    world.itemconfig(c12, window = cp12.config(text = '%02X' % seibutsu[ev][36*(seibutsu[ev][0] >= 9)]*(seibutsu[ev][0] >= 9)))
    world.itemconfig(c13, window = cp13.config(text = '%02X' % seibutsu[ev][40*(seibutsu[ev][0] >= 10)]*(seibutsu[ev][0] >= 10)))
    if sample:
        world.delete('sample')
    x, y = seibutsu[ev][2:4]
    for a in range(1, seibutsu[ev][0]+1):
        world.create_oval(seibutsu[ev][a*4-2]-x+883, seibutsu[ev][a*4-1]-y+368, seibutsu[ev][a*4-2]-x+887, seibutsu[ev][a*4-1]-y+372, outline = '#'+('%02x'%(((seibutsu[ev][a*4] & 0b11000000)>> 6 )*64+63))+('%02x'%(((seibutsu[ev][a*4] & 0b1100)>>2)*64+63))+('%02x'%((seibutsu[ev][a*4] & 0b11)*64+63)), fill = 'black', tags = 'sample')
    sample = True
#    if lookcell != False:
#        for deleting in lookcell:
#            canvas.delete(deleting)
#    for creating in range(seibutsu[ev][0]):
#    print(ev)

def move():
    global seibutsu
    global hiki
    global start
    global esa
    global foods
    global max
    global hosyoku
    global eatzatsu
    global dame
    global times
    global t_, T_, fps
    T_ = t_
    t_ = time.time()
    Fps=fps
    if t_-T_:
        fps = 1/(t_-T_)
    else:
        fps = 0xffff
    if start:
        if False:
            if (fps+Fps)/2 < 5:
                print('{:.3}'.format((fps+Fps)/2))
            else:
                print('{:3}'.format(int((fps+Fps)/2)))
        #move
        if foods < max:
            esaba = [ran(5, 805), ran(5, 805)]
            botsu = False
            for all in esa:
                if all[0] == esaba[0] and all[1] == esaba[1] and foods < max:
                    botsu = True
                    break
            if botsu != True:
                 esa.append(esaba + [world.create_line(esaba[0], esaba[1], esaba[0]+1, esaba[1]+1, fill = 'blue')])
                 botsu = False
                 foods += 1
            world.itemconfig(echo2, window = pfoods.config(text = str(foods)))
        else:
            esaba = [ran(5, 805), ran(5, 805)]
            botsu = False
            for all in esa:
                if all[0] == esaba[0] and all[1] == esaba[1]:
                    botsu = True
                    break
            if not botsu:
                vs = ran(0, foods-1)
                world.move(esa[vs][2], esaba[0] - esa[vs][0], esaba[1] - esa[vs][1])
                esa[vs][0:2] = esaba
        
        for b in seibutsu:
            prcnt = seibutsu[b][4] & 0x03
            to = (seibutsu[b][4] & 0x0c) >> 2
            if ran(0, 3+prcnt) >= 4:
                px = 0-(to == 0)+(to == 1)
                py = 0-(to == 2)+(to == 3)
            else:
                ido = ran(0, 3)
                px = 0-(ido == 0)+(ido == 1)
                py = 0-(ido == 2)+(ido == 3)
            for thec in range(2, (seibutsu[b][0]-1)*4+3, 4):
                kx = seibutsu[b][thec] + px
                ky = seibutsu[b][thec+1] + py
                kx += (kx < 5) * 800 - (kx > 805) * 800
                ky += (ky < 5) * 800 - (ky > 805) * 800
                world.move(seibutsu[b][thec+3], kx-seibutsu[b][thec], ky-seibutsu[b][thec+1])
                seibutsu[b][thec : thec+2] = [kx, ky]
                seibutsu[b][1] -= seibutsu[b][0]
        #add
        new = {}
        for a in seibutsu:
            b = seibutsu[a]
            c = b[0]
            dna = b[4+(c-1)*4]
            cdv = ((dna & 0x30) >> 4)+1
            eg = b[1]
            if eg > (0x1000*cdv*c) and hiki < 4096:
                id = 1
                while (id in seibutsu or id in new):
                    id = ran(1, 4096)
                if ran(0, val2.get()) == 0:
                    ndna = dna ^ (1 << ran(0, 7))
                    color = hex((int(((ndna & 0xc0) / 0x40) *64+63) << 16)\
                            +(int(((ndna & 0x0c) / 0x04) *64+63) << 8)\
                            +(int((ndna & 0x03) / 0x01) *64+63))
                    color = color.replace('0x', '#')
                    #for unb in range(5, 1+c*4, 4):
                    #    sleep(0)
                    if ran(0, 5) == 0:
                        ketsugo = (dna & 0xC0) >> 6
                        nx = b[2+(c-1)*4] + (ketsugo == 0)*(-4) + (ketsugo == 1) *4
                        ny = b[3+(c-1)*4] + (ketsugo == 2)*(-4) + (ketsugo == 3) *4
                        nx += (nx < 5) * 800 - (nx > 805) * 800
                        ny += (ny < 5) * 800 - (ny > 805) * 800
                        new[id] = b[:]
                        for d in range(5, (c-1)*4+5+1,4):
                            ocolor = hex((int(((seibutsu[a][d-1] & 0xc0) / 0x40) *64+63) << 16)\
                            +(int(((seibutsu[a][d-1] & 0x0c) / 0x04) *64+63) << 8)\
                            +(int((seibutsu[a][d-1] & 0x03) / 0x01) *64+63))
                            ocolor = ocolor.replace('0x', '#')
                            new[id][d] = world.create_oval(new[id][d-3]-2, new[id][d-2]-2, new[id][d-3]+2, new[id][d-2]+2, outline = ocolor, fill = 'black', tags = str(id))
                            world.tag_bind(new[id][d], '<Button-1>', click)
                        new[id][len(new[id]) : len(new[id])+4] = [nx, ny, ndna, world.create_oval(nx-2, ny-2, nx+2, ny+2, outline = color, fill = 'black', tags = str(id))]
                        world.tag_bind(new[id][-1], '<Button-1>', click)
                        new[id][0] += 1
                        new[id][1] = eg / 2
                    else:
                        new[id] = b[:]
                        for d in range(9, (c-1)*4+5+1,4):
                            ocolor = hex((int(((seibutsu[a][d-1] & 0xc0) / 0x40) *64+63) << 16)\
                            +(int(((seibutsu[a][d-1] & 0x0c) / 0x04) *64+63) << 8)\
                            +(int((seibutsu[a][d-1] & 0x03) / 0x01) *64+63))
                            ocolor = ocolor.replace('0x', '#')
                            new[id][d] = world.create_oval(new[id][d-3]-2, new[id][d-2]-2, new[id][d-3]+2, new[id][d-2]+2, outline = ocolor, fill = 'black')
                        new[id][1] = eg / 2
                        new[id][4] = ndna
                        new[id][5] = world.create_oval(seibutsu[a][2]-2, seibutsu[a][3]-2, seibutsu[a][2]+2, seibutsu[a][3]+2, outline = color, fill = 'black', tags = id)
                        world.tag_bind(new[id][5], '<Button-1>', click)
                    seibutsu[a][1] = eg / 2
                    hiki += 1
                    world.itemconfig(echo1, window = plives.config(text = str(hiki)))
                    #for unb in range(5, 1+new[id][0]*4, 4):
                    #    sleep(0)#world.itemunbind(new[unb], '<Button-1>')
                    #for unb in range(5, 1+new[id][0]*4, 4):
                    #    sleep(0)#world.itembind(new[unb], '<Button-1>', click(id))
                else:
                    new[id] = b[:]
                    for d in range(5, (c-1)*4+5+1,4):
                        color = hex((int(((seibutsu[a][d-1] & 0xc0) / 0x40) *64+63) << 16)\
                        +(int(((seibutsu[a][d-1] & 0x0c) / 0x04) *64+63) << 8)\
                        +(int((seibutsu[a][d-1] & 0x03) / 0x01) *64+63))
                        color = color.replace('0x', '#')
                        new[id][d] = world.create_oval(new[id][d-3]-2, new[id][d-2]-2, new[id][d-3]+2, new[id][d-2]+2, outline = color, fill = 'black', tags = id)
                        world.tag_bind(new[id][d], '<Button-1>', click)
                    new[id][1] = eg / 2
                    seibutsu[a][1] = eg /2
                    hiki += 1
                    world.itemconfig(echo1, window = plives.config(text = str(hiki)))
        for add in new:
            if start != True:
                break
            seibutsu[add] = new[add]
        #eat 
        botsu = 0
        dame = []
        for a in seibutsu:
            botsu = 0
            for b in range(2, (seibutsu[a][0]-1)*4+2+1, 4):
                if seibutsu[a][0] == 1 or eatzatsu:
                    for c in range(0, foods):
                        if c >= foods - botsu:
                            break
                        if esa[c][0] - seibutsu[a][b] <= 3 and esa[c][0] - seibutsu[a][b] >= -3 and esa[c][1] - seibutsu[a][b+1] <= 3 and esa[c][1] - seibutsu[a][b+1] >= -3:
                            seibutsu[a][1] += 0x500
                            foods -= 1
                            botsu += 1
                            world.itemconfig(echo2, window = pfoods.config(text = str(foods)))
                            world.delete(esa[c][2])
                            del esa[c]
                            break
                if seibutsu[a][0] != 1 and hosyoku:
                    for c in seibutsu:
                        f = False
                        for e in dame:
                            if a == e or c == e:
                                f = True
                                break
                        if a != c and not f:
                            for d in range(2, (seibutsu[c][0]-1)*4+2+1, 4):
                                if seibutsu[a][b] - seibutsu[c][d] <= 3 and seibutsu[a][b] - seibutsu[c][d] >= -3 and seibutsu[a][b+1] - seibutsu[c][d+1] <= 3 and seibutsu[a][b+1] - seibutsu[c][d+1] >= -3:
                                    seibutsu[a][1] += seibutsu[c][1]
                                    hiki -= 1
                                    dame.append(c)
                                    world.itemconfig(echo1, window = plives.config(text = str(hiki)))
                                    break
        for a in dame:
            for b in range(5, (seibutsu[a][0]-1)*4+5+1, 4):
                world.delete(seibutsu[a][b])
            del seibutsu[a]
        dame = []
        #die
        botsu = []
        for a in seibutsu:
            if seibutsu[a][1] <= 0:
                for d in range(5, (seibutsu[a][0]-1)*4+5+1, 4):
                    world.delete(seibutsu[a][d])
                botsu.append(a)
        for a in botsu:
            del seibutsu[a]
        hiki -= len(botsu)
        world.itemconfig(echo1, window = plives.config(text = str(hiki)))
        #add times
        times += 1
        returnclear(root.title(' Genes.py-'+version+' - '+str(times)+' 回目'))
        if recoding:
            root.after(1, recode)
        world.update()
        sleep(0.01)
        root.update()
    root.after(1, move)

def create_mine():
    subwin = tk.Toplevel(root)
    panel = tk.Canvas(subwin, width = 450, height = 370, bg = 'gray')
    panel.pack()
    panel.create_rectangle(10, 10, 150, 150, fill = 'black')
    cells = 0
    c_dna = ['', '', '', '', '', '', '', '', '', '']
    dna = 0xd0
    labels = [tk.Label(subwin, text = c_dna[0], bg = 'white', width = 8), \
            tk.Label(subwin, text = c_dna[1], bg = 'white', width = 8), \
            tk.Label(subwin, text = c_dna[2], bg = 'white', width = 8), \
            tk.Label(subwin, text = c_dna[3], bg = 'white', width = 8), \
            tk.Label(subwin, text = c_dna[4], bg = 'white', width = 8), \
            tk.Label(subwin, text = c_dna[5], bg = 'white', width = 8), \
            tk.Label(subwin, text = c_dna[6], bg = 'white', width = 8), \
            tk.Label(subwin, text = c_dna[7], bg = 'white', width = 8), \
            tk.Label(subwin, text = c_dna[8], bg = 'white', width = 8), \
            tk.Label(subwin, text = c_dna[9], bg = 'white', width = 8)]
    sub_widgets = []
    for a in range(10):
        panel.create_window(35, 165+a*21, window = tk.Label(subwin, text = 'Gene '+str(a), bg = 'gray'))
        sub_widgets.append(panel.create_window(100, 165+a*21, window = labels[a]))
    def addone():
        newdna = dna
    def delone():
        if cells != 0:
            c_dna[cells-1] = ''
            panel.delete(sub_widgets[-1])
            sub_widgets.pop()
            



def save():
    global name, path
    name = tkFileDialog.asksaveasfilename(filetypes = [('Genes Data Files', ('.gnsp', '.GNSP')), ('All Files', ('.*',))], initialdir = path)
    if name == '' or name == ():
        return
    with open(name, mode = 'w') as f:
        f.write(str([version, times, hiki, foods, max, kakuritu, hosyoku, eatzatsu]).replace('[', '').replace(']', '%').replace(', ', '#')+str(seibutsu).replace('{', ' ').replace('}', '%').replace('], ', ']#')+str(tuple(esa)).replace('(', '').replace(')', '').replace('], ', ']#'))

def load():
    global path, hiki, foods, max, kakuritu, hosyoku, eatzastu, seibutsu, esa, start, hatsu, times
    name = tkFileDialog.askopenfilename(filetypes = [('Genes Date Files', ('.gnsp', '.GNSP')), ('All Files', ('.*',))], initialdir = path)
    if name == '' or name == ():
        return
    start = False
    with open(name, mode = 'r') as f:
        data = f.read()
    f_ver = data.split('#')[0].replace("'", "").split('.')
    if not (int(old_ver.split('.')[0]) <= int(f_ver[0]) <= int(version.split('.')[0]) and int(old_ver.split('.')[1]) <= int(f_ver[1]) <= int(version.split('.')[1]) and int(old_ver.split('.')[2]) <= int(f_ver[2]) <= int(version.split('.')[2])):
        messagebox.showerror('バージョンエラー', 'この保存データのバージョンは使用バージョンと互換性がありません。\n保存データのバージョン: '+data.split('#')[0]+"\n使用バーション: "+version)
        return
    data = data.split('%')
    a = data[0]
    a = a.split('#')
    for b in range(0, len(a)):
        c = a[b]
        for d in range(0, 10):
            c = c.replace(str(d), '')
        if c == '':
            a[b] = int(a[b])
        if a[b] == 'True':
            a[b] = True
        if a[b] == 'False':
            a[b] = False
    f_ver, times, hiki, foods, max, kakuritu, hosyoku, eatzatsu = a
    #print(a)
    #print(max)
    #sleep(10)
    a = data[1]
    a = a.replace(' ', '').split('#')
    c = {}
    for b in range(0, len(a)):
        #print(a[b])
        a[b] = a[b].split(':')
        #print(a[b])
        a[b][1] = a[b][1].replace('[', '').replace(']', '').split(',')
        for d in range(0, len(a[b][1])):
            a[b][1][d] = float(a[b][1][d])
        c[int(a[b][0])] = a[b][1]
    if hatsu == False:
        for a in seibutsu:
            for b in range(5, 5+seibutsu[a][0]*4, 4):
                world.delete(seibutsu[a][b])
    seibutsu = c
    a = data[2].split('#')
    for b in range(0, len(a)):
        a[b] = a[b].replace('[', '').replace(']', '').split(', ')
        for c in range(0, 3):
            a[b][c] = int(a[b][c])
    if hatsu == False:
        for b in esa:
            world.delete(b[2])
    esa = a
    val1.set(max)
    val2.set(kakuritu)
    world.itemconfig(fm, window = scale1.config(label = 'FoodsMAX: '+str(max)))
    world.itemconfig(ka, window = scale2.config(label = 'Mutation(1/n): '+str(kakuritu)))
    world.itemconfig(echo1, window = plives.config(text = str(hiki)))
    world.itemconfig(echo2, window = pfoods.config(text = str(foods)))
    if hatsu:
        for sen in range(5, 806, 80):
            world.create_line(sen, 5, sen, 805, fill = 'green')
            world.create_line(5, sen, 805, sen, fill = 'green')
    for a in seibutsu:
        #print(seibutsu[a])
        seibutsu[a][0] = int(seibutsu[a][0])
        for b in range(1, seibutsu[a][0]+1):
            seibutsu[a][b*4] = int(seibutsu[a][b*4])
            seibutsu[a][b*4-2] = int(seibutsu[a][b*4-2])
            seibutsu[a][b*4-1] = int(seibutsu[a][b*4-1])
            color = '#'+('%02x'%(((seibutsu[a][b*4] & 0b11000000)>> 6 )*64+63))+('%02x'%(((seibutsu[a][b*4] & 0b1100)>>2)*64+63))+('%02x'%((seibutsu[a][b*4] & 0b11)*64+63))
            #print(color)
            seibutsu[a][b*4+1] = world.create_oval(seibutsu[a][b*4-2]-2, seibutsu[a][b*4-1]-2, seibutsu[a][b*4-2]+2, seibutsu[a][b*4-1]+2, fill = 'black', outline = color, tags = str(a))
            world.tag_bind(seibutsu[a][b*4+1], '<Button-1>', click)
    for a in range(0, len(esa)):
        esa[a][2] = world.create_line(esa[a][0], esa[a][1], esa[a][0], esa[a][1]+1, fill = 'blue')
    start = False
    hatsu = False
    returnclear(root.title(' Genes.py-'+version+' - '+str(times)+' 回目'))
    #print(seibutsu)
    #print(len(seibutsu))
    root.after(5, move)

def on_recode():
    global recode_name, path, recoding
    if not recoding:
        recode_name = tkFileDialog.asksaveasfilename(filetypes = [('Genes Recode Files', ('.gnsr', '.GNSR')), ('All Files', ('.*',))], initialdir = path)
        if recode_name == '' or recode_name == ():
            return
        with open(recode_name, mode = 'w') as f:
            f.write(str(old_ver)+'#'+str(version))
        recoding = 1
        #filemenu.itemconfig(menu_recode, label = 'Recode @')
    else:
        recoding = 0
        #filemenu.itemconfig(menu_recode, label = 'Recode  ')

def recode():
    with open(recode_name, mode = 'a') as f:
        f.write('&'+str([times, hiki, foods, max, kakuritu, hosyoku, eatzatsu]).replace('[', '').replace(']', '%').replace(', ', '#')+str(seibutsu).replace('{', ' ').replace('}', '%').replace('], ', ']#')+str(tuple(esa)).replace('(', '').replace(')', '').replace('], ', ']#'))
        #print(1)


def returnclear(text = ''):
    return









world = tk.Canvas(root, width = 965, height = 810)

world.pack()

world.create_rectangle(5, 5, 805, 805, fill = 'black')
world.create_rectangle(810, 5, 960, 250, fill = 'gray')
world.create_rectangle(810, 255, 960, 805, fill = 'gray')
world.create_rectangle(815, 300, 955, 440, fill = 'black')

plives = tk.Label(width = 9, text = hiki, bg = 'white')
pfoods = tk.Label(width = 9, text = foods, bg = 'white')

world.create_window(920, 40, window = tk.Button(width = 5, text = 'stop', command = buttonsto))
world.create_window(850, 40, window = tk.Button(width = 5, text = 'start', command = buttonsta))
world.create_window(850, 75, window = tk.Label(text = 'Lives', bg = 'gray'))
echo1 = world.create_window(910, 75, window = plives)
world.create_window(850, 100, window = tk.Label(text = 'Foods', bg = 'gray'))
echo2 = world.create_window(910, 100, window = pfoods)

scale1 = tk.Scale(label = 'FoodsMAX: '+'500', orient = 'h', from_ = 500, to = 4100, showvalue = False, variable = val1, length = 140, sliderlength = 15, resolution = 1, bg = 'gray', command = scl1)
scale2 = tk.Scale(label = 'Mutation(1/n): '+'10', orient = 'h', from_ = 0, to = 100, showvalue = False, variable = val2, length = 140, sliderlength = 15, resolution = 1, bg = 'gray', command = scl2)
fm = world.create_window(885, 140, window = scale1)
ka = world.create_window(885, 185, window = scale2)
world.create_window(885, 215, window = tk.Radiobutton(text = 'Multicellular is ...', variable = rdb1, value = True, command = caneat, bg = 'gray'))
world.create_window(885, 235, window = tk.Radiobutton(text = 'Omnivores Predator  ', variable = rdb2, value = True, command = eatall, bg = 'gray'))

cp1 = tk.Label(width = 9, text = str(cnumber), bg = 'white')
cp2 = tk.Label(width = 9, text = life, bg = 'white')
cp3 = tk.Label(width = 9, text = cells, bg = 'white')
cp4 = tk.Label(width = 9, text = ce1, bg = 'white')
cp5 = tk.Label(width = 9, text = ce2, bg = 'white')
cp6 = tk.Label(width = 9, text = ce3, bg = 'white')
cp7 = tk.Label(width = 9, text = ce4, bg = 'white')
cp8 = tk.Label(width = 9, text = ce5, bg = 'white')
cp9 = tk.Label(width = 9, text = ce6, bg = 'white')
cp10 = tk.Label(width = 9, text = ce7, bg = 'white')
cp11 = tk.Label(width = 9, text = ce8, bg = 'white')
cp12 = tk.Label(width = 9, text = ce9, bg = 'white')
cp13 = tk.Label(width = 9, text = ce10, bg = 'white')

world.create_window(850, 275, window = tk.Label(text = 'Clicked\nCreat', bg = 'gray'))
c1 = world.create_window(910, 275, window = cp1)
world.create_window(850, 460, window = tk.Label(text = 'Life', bg = 'gray'))
c2 = world.create_window(910, 460, window = cp2)
world.create_window(850, 480, window = tk.Label(text = 'Cells', bg = 'gray'))
c3 = world.create_window(910, 480, window = cp3)
world.create_window(850, 510, window = tk.Label(text = 'Gene 0', bg = 'gray'))
c4 = world.create_window(910, 510, window = cp4)
world.create_window(850, 530, window = tk.Label(text = 'Gene 1', bg = 'gray'))
c5 = world.create_window(910, 530, window = cp5)
world.create_window(850, 550, window = tk.Label(text = 'Gene 2', bg = 'gray'))
c6 = world.create_window(910, 550, window = cp6)
world.create_window(850, 570, window = tk.Label(text = 'Gene 3', bg = 'gray'))
c7 = world.create_window(910, 570, window = cp7)
world.create_window(850, 590, window = tk.Label(text = 'Gene 4', bg = 'gray'))
c8 = world.create_window(910, 590, window = cp8)
world.create_window(850, 610, window = tk.Label(text = 'Gene 5', bg = 'gray'))
c9 = world.create_window(910, 610, window = cp9)
world.create_window(850, 630, window = tk.Label(text = 'Gene 6', bg = 'gray'))
c10 = world.create_window(910, 630, window = cp10)
world.create_window(850, 650, window = tk.Label(text = 'Gene 7', bg = 'gray'))
c11 = world.create_window(910, 650, window = cp11)
world.create_window(850, 670, window = tk.Label(text = 'Gene 8', bg = 'gray'))
c12 = world.create_window(910, 670, window = cp12)
world.create_window(850, 690, window = tk.Label(text = 'Gene 9', bg = 'gray'))
c13 = world.create_window(910, 690, window = cp13)
menu = tk.Menu(root)
root.configure(menu = menu)
filemenu = tk.Menu(menu, tearoff = False)
optionmenu = tk.Menu(menu, tearoff = False)
menu.add_cascade(label = 'File', underline = 0, menu = filemenu)
menu.add_cascade(label = 'Options', underline = 0, menu = optionmenu)
filemenu.add_command(label = 'Save', underline = 0, command = save)
filemenu.add_command(label = 'Load', underline = 0, command = load)
optionmenu.add_command(label = 'Create...', underline = 0, command = create_mine)
#menu_recode = filemenu.add_command(label = 'Recode  ', underline = 0, command = on_recode)
#root.after(1, get_temp)
#root.after(1000, load)
root.mainloop()
#save()

