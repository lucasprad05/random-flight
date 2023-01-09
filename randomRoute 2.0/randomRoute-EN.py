#Random Route
#by Lucas Prado

from __future__ import print_function
from tkinter import *
from unicodedata import name
from PythonMETAR import *
import random, os, sys, getopt, string
from PIL import Image,ImageTk
import webbrowser

try:
    from urllib3 import urlopen
except:
    from urllib.request import urlopen
from metar import Metar

BASE_URL = "http://tgftp.nws.noaa.gov/data/observations/metar/stations"
SIMBRIEF_URL = 'https://www.simbrief.com/system/login.sso.php?ref=http%3A%2F%2Fwww.simbrief.com%2Fhome%2F'
VREF_URL = 'https://www.vrefsimulations.com/'
BACKGROUND = '#414141'
BTN_COLOR = '#202020'
COLOR = '#6b6b6b'
TXT_COLOR = 'white'

class MyWindow:
    
    def __init__(self, win):
        self.my_list = []

        self.lbl_icao = Label(win, text='Airport ICAO', bg=BACKGROUND, fg=TXT_COLOR)
        self.lbl_icao.place(x = 20, y = 20)
        self.t_icao = Entry(bg=COLOR, fg=TXT_COLOR)
        self.t_icao.place(x = 100, y = 20, width = 40)

        self.lbl_route = Label(win, text='Route', bg=BACKGROUND, fg=TXT_COLOR)
        self.lbl_route.place(x = 20, y = 110)
        self.t_route = Entry(bg=COLOR, fg=TXT_COLOR)
        self.t_route.place(x = 65, y = 110, width = 80)

        self.btn_add = Button(win, text='Add', command = self.add, bg=BTN_COLOR, fg=TXT_COLOR)
        self.btn_add.place(x = 30, y = 60)

        self.btn_pick = Button(win, text='Pick', command = self.sort, bg=BTN_COLOR, fg=TXT_COLOR)
        self.btn_pick.place(x = 80, y = 60)

        #-----------------------------------------------------
        #VREF
        self.vref_logo = Image.open('vref_logo.png')
        self.vref_logo = self.vref_logo.resize((80,50), Image.Resampling.LANCZOS)
        self.img_vref= ImageTk.PhotoImage(self.vref_logo)
        self.btn_vref= Button(win, image=self.img_vref, compound= LEFT, command=self.vref, borderwidth=0)
        self.btn_vref.place(x = 185, y = 20)


        #-----------------------------------------------------
        #SIMBRIEF

        self.simbrief_logo = Image.open('simbrief.png')
        self.simbrief_logo = self.simbrief_logo.resize((50,50), Image.Resampling.LANCZOS)
        self.img= ImageTk.PhotoImage(self.simbrief_logo)
        self.btn_sb= Button(win, image=self.img, compound= LEFT, command=self.simbrief, borderwidth=0)
        self.btn_sb.place(x = 200, y = 90)

        #-----------------------------------------------------
        #Metar

        self.lbl_metar = Label(win, text='METAR ->', bg=BACKGROUND, fg=TXT_COLOR)
        self.lbl_metar.place(x = 20, y = 160)
        
        self.t_readM1 = Text(win, height=3, width = 30, bg=COLOR, fg=TXT_COLOR)
        self.t_readM1.place(x = 30, y = 190)
        
        self.t_readM2 = Text(win, height=3, width = 30, bg=COLOR, fg=TXT_COLOR)
        self.t_readM2.place(x = 30, y = 250)

        #-----------------------------------------------------
        #Internet Connection

        internet_connection = self.connection()
        print(internet_connection)
        #internet_connection = True

        if internet_connection == True:
            self.lbl_netOn = Label(win, text='Connected to internet', fg='#128227', bg=BACKGROUND)
            self.lbl_netOn.place(x = 10, y = 330)
        else:
            self.lbl_netOff = Label(win, text='No internet avaiable', fg='#fc0303', bg=BACKGROUND)
            self.lbl_netOff.place(x = 10, y = 330)

        #-----------------------------------------------------
        #Dev credits

        self.lbl_dev = Label(win, text='Developed by Lucas Prado', fg=TXT_COLOR, bg=BACKGROUND)
        self.lbl_dev.place (x = 165, y = 330)

    def connection(self):
        try:
            host = 'https://www.google.com.br'
            urlopen(host)
            return True
        except:
            return False

    def vref(self):
        webbrowser.open(VREF_URL)

    def simbrief(self):
        webbrowser.open(SIMBRIEF_URL)

    def add(self):
        apt = self.t_icao.get()
        self.my_list.append(apt)
        self.t_icao.delete(0, 'end')

    def sort(self):
        self.t_route.delete(0, 'end')
        N = len(self.my_list) - 1
        apt_icao = random.randint(0, N)
        apt_route = random.randint(0, N)
        if self.my_list[apt_icao] == self.my_list[apt_route]:
            return self.sort()

        self.t_route.insert(END, f"{self.my_list[apt_icao].upper()}  -  {self.my_list[apt_route].upper()}")
        nameApt_icao = self.my_list[apt_icao].upper()
        nameApt_route = self.my_list[apt_route].upper()
        metar1 = self.metar(nameApt_icao)
        metar2 = self.metar(nameApt_route)

        self.t_readM1.insert(END, metar1)
        self.t_readM2.insert(END, metar2)



    def usage(self):
        def usage(): #test to delete this line
            program = os.path.basename(sys.argv[0])
            sys.exit(1)

    def metar(self, sApt):
        stations = []
        debug = False

        try:
            opts, stations = getopt.getopt(sys.argv[1:], "d")
            for opt in opts:
                if opt[0] == "-d":
                    debug = True
        except:
            self.usage()

        if not stations:
            self.usage()

        url = "%s/%s.TXT" % (BASE_URL, sApt)

        if debug:
            sys.stderr.write("[ " + url + " ]")
        try:
            urlh = urlopen(url)
            report = ""
            for line in urlh:
                if not isinstance(line, str):
                    line = line.decode()  # convert Python3 bytes buffer to string
                if line.startswith(sApt):
                    report = line.strip()
                    obs = Metar.Metar(line)
                    #print(obs.string())
                    break

            if not report:
                return "no data avaiable"

        except Metar.ParserError as exc:
            #print("METAR ", sApt, ": ", line)
            #print(string.join(exc.args, ", "), "\n")
            pass

        except:
            import traceback
            # print(traceback.format_exc())
            # print("Error retrieving", sApt, "data", "\n")
            pass
        
        return line


window = Tk()
mywin = MyWindow(window)
window.title('Random Route')
window.iconbitmap('iconPlane.ico')
window.geometry("310x350")
window.resizable(width = False, height = False)
window.configure(background=BACKGROUND)
window.mainloop()