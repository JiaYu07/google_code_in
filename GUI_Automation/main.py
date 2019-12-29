import os
import tkinter as tk
import webbrowser

def open_github():
    webbrowser.open(url="https://github.com/")


def open_vscode():
    os.system("code . ")


def open_playlist():
    path= "/home/crystal/桌面/google_code_in/GUI_Automation/music_list.m3u8"
    os.system("xdg-open "+ path) 
     

def main():
    gui= tk.Tk()
    gui.title("Python Automation App")
    gui.geometry("480x360")
    gui.configure(background="white")
    toGitHub_btn = tk.Button(gui, text='Open GitHub',activebackground="grey",command=open_github).pack()
    toVscode_btn = tk.Button(gui, text='Open Vscode',activebackground="grey",command=open_vscode).pack()
    playMusic_btn = tk.Button(gui, text='Play Music List',activebackground="grey",command=open_playlist).pack()

    gui.mainloop()


if __name__=="__main__":
    main()
