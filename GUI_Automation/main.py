import os
import tkinter as tk
import webbrowser

def open_github():
    webbrowser.open()


def open_vscode():
    os.system("code . ")


def open_playlist():
    path=/home/crystal/桌面/google_code_in/GUI_Automation/music_list/play_list.m3u
     os.system("xdg-open",path) 
     

def main():



if __name__=="__main__":
    main()
