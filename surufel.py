# https://github.com/Surufel/surufel-scanner

import sys
import os

import pyclamd
import virus_total_apis

import psycopg2

# Python 2
#import Tkinter
#import tkMessageBox

# Python 3
import tkinter
from tkinter import messagebox
from tkinter import filedialog

from tkinter import *
from tkinter.ttk import *

# I do not want to support py2. Just a warning.

class SiferCore:
    '''A Surufel '''
    def __init__(self):
        pass

    def startHere():
        pass

    def connect():
        ''' Connect to database. '''
        pass

    def scan():
        # create traverse function?
        # scan each file based on criteria in db from connect()

        pass

class SurufelCore:
    '''A Surufel core that does the magic.'''
    version = 1.8
    filesScannedCount = 0

    # Root
    front = tkinter.Tk()
    front.geometry('650x400+0+0')
    front.title("Surufel Scanner")
    front.resizable(0,0)

    # Frames
    frame1 = tkinter.Frame(front, bg='#ECECEC', width=50, height=400, padx=0, pady=0)
    frame1.pack(side='left', expand=0, fill='both')

    frame2 = tkinter.Frame(front, bg='white', width=600, height=400, padx=0, pady=0)
    frame2.pack(side='right', expand=1, fill='both')

    style = tkinter.ttk.Style()
    style.configure("TButton", foreground="black", background="#8B7B8B", width=26)
    style.theme_use('aqua')

    def __init__(self):
        if sys.platform == "darwin":
            try:
                self.scanner = pyclamd.ClamdAgnostic()
                self.scanner.ping()
            except pyclamd.ConnectionError:
                self.scanner = pyclamd.ClamdNetworkSocket()
                try:
                    self.scanner.ping()
                except pyclamd.ConnectionError:
                    raise ValueError('I could not connect to Unix or network socket.')
        elif sys.platform == "linux":
            pass
        elif sys.platform == "win32":
            # One day.
            pass

    def reloadCallback(self):
        ''' Reload ClamAV related files. '''
        reloadMessage = self.scanner.reload()
        reloadOutput = tkinter.Message(self.frame2, bg='white', width=400, text=reloadMessage)
        reloadOutput.pack(side='top', fill='both')
        reloadOutput.after(5000, reloadOutput.pack_forget)

    def versionCallback(self):
        ''' Version of the program. '''
        versionMessage = "Version: " + str(self.version) + "\n" + "pyClamd Version: " + self.scanner.version()
        #messagebox.showinfo("Version", versionMessage)
        versionOutput = tkinter.Message(self.frame2, bg='white', width=400, text=versionMessage)
        versionOutput.pack(side='top', fill='both')
        versionOutput.after(5000, versionOutput.pack_forget)

    def fileScanner(self, file):
        '''This will return the file with its absolute path.'''
        return self.scanner.scan_file(os.path.abspath(file))

    def browseFilesToScan(self):
        ''' Select file to scan. '''
        fileName = filedialog.askopenfilename(title = "Select file", filetypes=())
        scanMessage = fileName + " might be clean."
        if (self.fileScanner(fileName)) is None:
            scanOutput = tkinter.Message(self.frame2, bg='white', width=400, text=scanMessage)
            scanOutput.pack(side='top', fill='both')
        scanOutput.after(5000, scanOutput.pack_forget)

    def scanCurrentDirectory(self):
        '''This will scan the current directory.'''
        path = "."
        dirs = os.listdir(path)

        currentDirectory = tkinter.Listbox(self.frame2, width=400)
        currentDirectory.pack()
        for files in dirs:
            if (self.fileScanner(files)) is None:
                self.filesScannedCount = self.filesScannedCount + 1
                fileScannedMessage = files + " might be clean."
                currentDirectory.insert('end', fileScannedMessage)
                countMessage = "Files counted: " + str(self.filesScannedCount)

        countOutput = tkinter.Message(self.frame2, bg='white', width=400, text=countMessage)
        countOutput.pack(side='top', fill='both')
        self.filesScannedCount = 0
        currentDirectory.after(15000, currentDirectory.pack_forget)
        countOutput.after(15000, countOutput.pack_forget)

    def scanCurrentDirectoryNoHidden(self):
        '''This will scan the current directory sans hidden files or directories.'''
        dirs = os.listdir(".")

        currentDirectoryNoHid = tkinter.Listbox(self.frame2, width=400)
        currentDirectoryNoHid.pack()
        for files in dirs:
            if (not files.startswith('.')) and ((self.fileScanner(files)) is None):
                self.filesScannedCount = self.filesScannedCount + 1
                fileScannedMessage = files + " might be clean."
                currentDirectoryNoHid.insert('end', fileScannedMessage)
                countMessage = "Files counted: " + str(self.filesScannedCount)

        countOutput = tkinter.Message(self.frame2, bg='white', width=400, text=countMessage)
        countOutput.pack(side='top', fill='both')
        self.filesScannedCount = 0
        currentDirectoryNoHid.after(15000, currentDirectoryNoHid.pack_forget)
        countOutput.after(15000, countOutput.pack_forget)

        # I could combine the two scanCurrentDirectory methods with the use of an additional parameter but I wanted to use startswith(). Backburner.

    def scannerMainframe(self):
        '''The GUI.'''
        # Root
        #front = tkinter.Tk()
        #front.geometry('650x400+0+0')
        #front.title("Surufel Scanner")

        # Frames
        #frame1 = tkinter.Frame(front, bg='#8B7B8B', width=50, height=400, padx=0, pady=0)
        #frame1.pack(side='left', expand=0, fill='both')

        logo = tkinter.Label(self.frame1, font='Arial 30 bold', text="Surufel", bg='#ECECEC', fg='black', height=3, width=10, padx=10, pady=0, borderwidth=2) #relief='groove'
        logo.pack()

        #browse = tkinter.Button(self.frame1, highlightbackground='#8B7B8B', text="Scan File", width=25, command=self.browseFilesToScan)
        browse = tkinter.ttk.Button(self.frame1, style="TButton", text="Scan File", command=self.browseFilesToScan)
        browse.pack()

        #scanCurDir = tkinter.Button(self.frame1, highlightbackground='#8B7B8B', text="Scan Currect Directory", width=25, command=self.scanCurrentDirectory)
        scanCurDir = tkinter.ttk.Button(self.frame1, style="TButton", text="Scan Current Directory", command=self.scanCurrentDirectory)
        scanCurDir.pack()

        #scanCurDirNoHid = tkinter.Button(self.frame1, highlightbackground='#8B7B8B', text="Scan Currect Directory (No Hidden)", width=25, command=self.scanCurrentDirectoryNoHidden)
        scanCurDirNoHid = tkinter.ttk.Button(self.frame1, style="TButton", text="Scan Current Directory (No Hidden)", command=self.scanCurrentDirectoryNoHidden)
        scanCurDirNoHid.pack()

        #reloadButton = tkinter.Button(self.frame1, highlightbackground='#8B7B8B', text="Reload", width=25, command=self.reloadCallback)
        reloadButton = tkinter.ttk.Button(self.frame1, style="TButton", text="Reload", command=self.reloadCallback)
        reloadButton.pack()

        #versionButton = tkinter.Button(self.frame1, highlightbackground='#8B7B8B', text="Version", width=25, command=self.versionCallback)
        versionButton = tkinter.ttk.Button(self.frame1, style="TButton", text="Version", command=self.versionCallback)
        versionButton.pack()

        #quitButton = tkinter.Button(self.frame1, highlightbackground='#8B7B8B', text="Quit", width=25, command=quit)
        quitButton = tkinter.ttk.Button(self.frame1, style="TButton", text="Quit", command=quit)
        quitButton.pack()

        #frame2 = tkinter.Frame(self.front, bg='#ffffff', width=600, height=400, padx=0, pady=0)
        #frame2.pack(side='right', expand=1, fill='both')

        title = "Scanner"
        theTitle = tkinter.Label(self.frame2, justify='left', width=400, height=2, text=title)
        theTitle.pack(fill='both')



        # Loop
        self.front.mainloop()

        # https://docs.python.org/3.3/library/tkinter.ttk.html
        # https://github.com/RedFantom/ttkthemes
        # I could use the ttk module but I need to focus on other areas. Backburner.

def main():
    firstRun = SurufelCore()
    firstRun.scannerMainframe()

    firstSiferRun = SiferCore()
    #

if __name__ == '__main__':
    main()
