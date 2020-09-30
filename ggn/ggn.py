import threading
import tkinter as Tk
# the client for ggntalk-pro
import time
import traceback
import socket
import os

title = """
__        ___                     _   _                     _
\\ \\      / / |__   ___ _ __ ___  | |_| |__   ___ _ __ ___  (_)___
 \\ \\ /\\ / /| '_ \\ / _ \\ '__/ _ \\ | __| '_ \\ / _ \\ '__/ _ \\ | / __|
  \\ V  V / | | | |  __/ | |  __/ | |_| | | |  __/ | |  __/ | \\__ \\
   \\_/\\_/  |_| |_|\\___|_|  \\___|  \\__|_| |_|\\___|_|  \\___| |_|___/

             _   _                 _____    _   _                     _
 _ __  _   _| |_| |__   ___  _ __ |___ /   | |_| |__   ___ _ __ ___  (_)___
| '_ \\| | | | __| '_ \\ / _ \\| '_ \\  |_ \\   | __| '_ \\ / _ \\ '__/ _ \\ | / __|
| |_) | |_| | |_| | | | (_) | | | |___) |  | |_| | | |  __/ | |  __/ | \\__ \\
| .__/ \\__, |\\__|_| |_|\\___/|_| |_|____( )  \\__|_| |_|\\___|_|  \\___| |_|___/
|_|    |___/                           |/
                   _        _ _
  __ _  __ _ _ __ | |_ __ _| | | __
 / _` |/ _` | '_ \\| __/ _` | | |/ /
| (_| | (_| | | | | || (_| | |   < _
 \\__, |\\__, |_| |_|\\__\\__,_|_|_|\\_(_)
 |___/ |___/
"""

#PORT = int(input("[ggntalk-client] input PORT>>>"))

def csnd(msg, show = True, HOST = "106.13.174.3",\
        BUFSIZ = 1024 * 1024 * 32): # try to connect with the server
    global port
    try:
        ADDR = (HOST, int(port.get()))
    except:
        global message
        message.delete(1.0, Tk.END)
        message.insert(Tk.END, "port is not available.")
        return

    tcp = socket.socket(socket.AddressFamily.AF_INET,\
    	socket.SOCK_STREAM)
    # tcp protocol, pay attention to the prefix of the const
    try:
        if show:
            print("[ggntalk-client] [csnd] trying to connect to " + HOST)
        tcp.connect(ADDR)
    except:
        if(show):
            print(traceback.format_exc())
        return "#error: can not connect to the server."
        # an string begin with '#' means an error
    else:
        if(show):
            print("[ggntalk-client] sending msg to server ...")
        tcp.send(msg.encode())
        if(show):
            print("[ggntalk-client] getting msg from server ...")
        ret = tcp.recv(BUFSIZ).decode() # return msg from server
        tcp.close() # close the connection
        return ret

"""
print(title)

print("[ggntalk-client] do you want to make it an output screen.")
print("1. Yes          2. No           Else.Quit")
ins = int(input("[ggntalk-client] input a number>>>"))

if ins == 1:
    print("[warning] you can only use Ctrl-C to kill this screen.")
    fname = input("[ggntalk-client] input your user name>>>")
    os.system("clear")
    print("-------------------- the chatting messages are listed as follows.\n")
    while True:
        ret = csnd("get$" + fname, False)
        if (ret != ""):
            print(ret)
            ret = csnd("write$" + fname + "$", False)
            print(ret)
            
elif ins == 2:
    while True:
        print("[ggntalk-client] choose from the following instructions.")
        print("1. Chat          2. Upload file          3. Download file          Else. Quit")
        ins = int(input("[ggntalk-client] input a number>>>"))
        if ins == 1:
            fname = input("[Chat] who do you want to chat with (use $ to seperate two names)>>>")
            uname = input("[Char] input your name>>>")
            print("[Chat] input an empty line to quit.")
            while True:
                msg = input(">>>")
                if(msg == ""):
                    break
                else:
                    ans = ""
                    if(msg[0] != "$"):
                        ans = msg
                    else:
                        print("[ggntalk-client] sending an output of a program ...")
                        tmp = msg[1:]
                        os.system(tmp + " >tmp")
                        fi = open("tmp", "r")
                        ans = "\n" + fi.read()
                        fi.close()
                        print("[ggntalk-client] program output get.")

                    nlis = fname.split("$")
                    nlis.append(uname)

                    for nm in nlis:
                        ret = csnd("append$" + nm + "$" + time.ctime() + "\t" + uname + ":\t" + ans+"\n")
                        print(ret)
                    
                    #time.sleep(0.1)
                    #csnd("append$" + uname + "$" + time.ctime() + "\t" + uname + ":\t" + msg)

        elif ins == 2:
            fname = input("[Upload] input file path(name)>>>")
            lname = input("[Upload] input the name used to store on server>>>")
            flag = int(input("[Upload] Are you sure to upload this file? (1. Yes / Else. No)>>>"))
            if(flag == 1):
                fi = open(fname, "r")
                msg = fi.read()
                fi.close()
                ret = csnd("write$" + lname + "$" + msg)
                print(ret)
            else:
                print("[Upload] give up successfully.")
        elif ins == 3:
            lname = input("[DownLoad] input the filename on server>>>")
            fname = input("[DownLoad] input the name used to store in this comuter>>>")
            flag = int(input("[DownLoad] are you sure to down load this file? (1. Yes / Else. No)"))
            if flag == 1:
                ret = csnd("get$" + lname)
                fi = open(fname, "w")
                fi.write(ret)
                fi.close()
                print("[DownLoad] successfully.")
            else:
                print("[DownLoad] give up successfully.")
        else:
            print("[ggntalk-client] quit and exit")
            break
else:
    print("[ggntalk-client] quit and exit.")
    exit(0)
    """
    

def refresh():
    global uname
    global pwd
    global wlog
    global message
    global gui
    message.delete(0.0, Tk.END) # delete all message before
    
    while wlog:
        print("[refresh] start refresh ...")
        ret = csnd("get$" + uname.get() + "$" + pwd.get() + "$novalue")
        #ret = ret.replace("\n", "")
        if(ret != "" and ret != " "):
            #global message
            gui.wm_attributes("-topmost", 1)
            message.insert(0.0, ret+"\n")
            ret = csnd("write$" + uname.get() + "$" + pwd.get() + "$" + uname.get() + "$ ")
            print(ret)
        gui.wm_attributes("-topmost", 0)

        time.sleep(0.5)

wlog = False # no log in

#th = None

def login():
    global wlog
    
    if wlog:
        print("[login] you have logged in.")
        global message
        message.delete(1.0, Tk.END)
        message.insert(Tk.END, "[login] you have logged in.")
        return

    #wlog = True

    #global text
    #print(text.get())
    global uname
    global pwd

    ret = csnd("append$" + uname.get() + "$" + pwd.get() +"$" + uname.get() + "$[login] " + time.ctime())
    #print(ret)
    if(ret == "[ggntalk-server] append successfully."):
        wlog = True
        print("login successfully.")
        uname.configure(state = "readonly") # lock it
        pwd.configure(state = "readonly")
        uto.configure(state = "normal")
        inp.configure(state = "normal")
        
        global port
        port.configure(state = "readonly")

        #global th
        th = threading.Thread(target = refresh)
        th.setDaemon(True)
        th.start() # a new thread
    else:
        print(ret)

def register():
    global message
    if wlog:
        print("[register] you have logged in.")
        message.delete(1.0, Tk.END)
        message.insert(Tk.END, "[register] you have logged in.")
        return

    global uname
    global pwd
    ret = csnd("register$" + uname.get() + "$" + pwd.get())
    print(ret)
    message.delete(1.0, Tk.END)
    message.insert(Tk.END, ret+"\n")

def stop():
    global uname
    global pwd
    if(uname.get() == "admin" and pwd.get()=="123456"):
        ret = csnd("stop")
        print(ret)
    else:
        print("[ggntalk-client] not admin.")
        global message
        message.delete(1.0, Tk.END)
        message.insert(Tk.END, "[stop] you are not admin")

def logout():
    #if th != None
    global message
    global wlog

    if not wlog:
        message.delete(1.0, Tk.END)
        message.insert(Tk.END, "you haven't logged in.")
        return

    message.delete(1.0, Tk.END)
    message.insert(Tk.END, "log out successfully.")

    wlog = False # log out
    global uname
    uname.configure(state = "normal")
    global port
    port.configure(state = "normal")
    global pwd
    pwd.configure(state = "normal")
    global uto
    uto.delete(0, Tk.END)
    uto.configure(state = "readonly")
    global inp
    inp.delete(0, Tk.END)
    inp.configure(state = "readonly")

gui = Tk.Tk()
gui.title("ggntalk-pro")
gui.geometry("400x600")

menus = Tk.Menu() # create a menu
menus.add_command(label = "login", command = login)
menus.add_command(label = "register", command = register)
menus.add_command(label = "stop", command = stop)
menus.add_command(label = "logout", command = logout)
gui.config(menu = menus)

label_port = Tk.Label(gui, text = "port")
label_port.pack(anchor = "w")

port = Tk.Entry(gui, width = 40)
port.pack(anchor = "e")

label_name = Tk.Label(gui, text = "ID")
label_name.pack(anchor = "w")

uname = Tk.Entry(gui, width = 40) # create a text box
uname.pack(anchor = "e")

label_pwd = Tk.Label(gui, text = "password")
label_pwd.pack(anchor = "w")

pwd = Tk.Entry(gui, width = 40, show = "*")
pwd.pack(anchor = "e")

#btn = Tk.Button(gui, text = "login", width = 10, height = 2, command = login)     # create a button
#btn.pack()

message = Tk.Text(gui, width = 50, height = 18)
message.pack(anchor = "w")

label_to = Tk.Label(gui, text = "to")
label_to.pack(anchor = "w")

uto = Tk.Entry(gui, width = 40, state = "disabled")
uto.pack(anchor = "e")

label_inp = Tk.Label(gui, text = "input")
label_inp.pack(anchor = "w")

gui.resizable(0, 0)

def getf(filename):
    fi = open(filename)
    ans = fi.read()
    fi.close()
    return ans

def send():
    global inp
    global uto
    global uname
    global pwd
    global message
    
    if uto.get() == "":
        print("[send] you can not send to no body.")
        message.delete(1.0, Tk.END)
        message.insert(Tk.END, "[send] you can not send to no body.")
        return

    if inp.get() == "":
        print("[send] you can not send an empty string.")
        message.delete(1.0, Tk.END)
        message.insert(Tk.END, "[send] you can not send an empty string.")
        return

    if not wlog:
        print("[send] you haven't logged in.")
        message.delete(1.0, Tk.END)
        message.insert(Tk.END, "you haven't logged in.")
        return

    lis = uto.get().split("$")
    lis.append(uname.get())

    ans = ""
    if inp.get()[0] != "$":
        ans = inp.get()
    else:
        ans = inp.get()[1:] + ">tmp"
        os.system(ans)
        ans = "\n" + getf("tmp")
        

    for x in lis:
        ret = csnd("append$" + uname.get() + "$" + pwd.get() + "$" + x + "$" + time.ctime() + ":" + uname.get() + ":\n>>>" + ans)
        print(ret)
    inp.delete(0, Tk.END)

inp = Tk.Entry(gui, width = 50, state = "disabled")
inp.pack(anchor = "w")

snd = Tk.Button(gui, text = "send", command = send)
snd.pack(anchor = "e")


gui.mainloop() # main loop