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

# I do not want to support py2. Just a warning.

class SiferCore:
    '''A Surufel '''
    def __init__(self):
        pass

    def startHere():
        pass

    def connect():
        pass

    def scan():
        # create traverse function?
        # scan each file based on criteria in db from connect()

        pass

class SurufelCore:
    '''A Surufel core that does the magic.'''
    version = 1.6
    filesScannedCount = 0

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
        print(self.scanner.reload())

    def versionCallback(self):
        versionMessage = "Surufel Version: " + str(self.version) + "\n" + "pyClamd Version: " + self.scanner.version()
        messagebox.showinfo("Version", versionMessage)

    def fileScanner(self, file):
        '''This will return the file with its absolute path.'''
        return self.scanner.scan_file(os.path.abspath(file))

    def scanCurrentDirectory(self):
        '''This will scan the current directory.'''
        path = "."
        dirs = os.listdir(path)

        for files in dirs:
            if (self.fileScanner(files)) is None:
                self.filesScannedCount = self.filesScannedCount + 1
                fileScannedMessage = files + " might be clean."
                print(fileScannedMessage)
                countMessage = "\nFiles counted: " + str(self.filesScannedCount)

        print(countMessage)
        self.filesScannedCount = 0

    def scanCurrentDirectoryNoHidden(self):
        '''This will scan the current directory sans hidden files or directories.'''
        dirs = os.listdir(".")

        for files in dirs:
            if (not files.startswith('.')) and ((self.fileScanner(files)) is None):
                self.filesScannedCount = self.filesScannedCount + 1
                fileScannedMessage = files + " might be clean."
                print(fileScannedMessage)
                countMessage = "\nFiles counted: " + str(self.filesScannedCount)

        print(countMessage)
        self.filesScannedCount = 0

        # I could combine the two scanCurrentDirectory methods with the use of an additional parameter but I wanted to use startswith(). Backburner.

    def scannerMainframe(self):
        '''The GUI.'''
        # Root
        front = tkinter.Tk()
        front.geometry('650x400+0+0')
        front.title("Surufel Scanner")

        # Frames
        frame1 = tkinter.Frame(front, bg='#8B7B8B', width=50, height=400, padx=0, pady=0)
        frame1.pack(side='left', expand=0, fill='both')

        logo = tkinter.Label(frame1, font='Arial 30 bold', text="Surufel", bg='#8B7B8B', fg='white', height=3, width=10, padx=10, pady=0, borderwidth=2) #relief='groove'
        logo.pack()

        scanCurDir = tkinter.Button(frame1, highlightbackground='#8B7B8B', text="Scan Currect Directory", width=25, command=self.scanCurrentDirectory)
        scanCurDir.pack()

        scanCurDirNoHid = tkinter.Button(frame1, highlightbackground='#8B7B8B', text="Scan Currect Directory (No Hidden)", width=25, command=self.scanCurrentDirectoryNoHidden)
        scanCurDirNoHid.pack()

        reloadButton = tkinter.Button(frame1, highlightbackground='#8B7B8B', text="Reload", width=25, command=self.reloadCallback)
        reloadButton.pack()

        versionButton = tkinter.Button(frame1, highlightbackground='#8B7B8B', text="Version", width=25, command=self.versionCallback)
        versionButton.pack()

        quitButton = tkinter.Button(frame1, highlightbackground='#8B7B8B', text="Quit", width=25, command=quit)
        quitButton.pack()

        frame2 = tkinter.Frame(front, bg='#ffffff', width=600, height=400, padx=0, pady=0)
        frame2.pack(side='right', expand=1, fill='both')

        title = "Scanner"
        theTitle = tkinter.Label(frame2, justify='left', width=600, height=2, text=title)
        theTitle.pack(fill='both')

        output = ": Program Information"
        theOutput = tkinter.Message(frame2, bg='blue', width=600, text=output)
        theOutput.pack(side='top', fill='both')

        #http://python-future.org/compatible_idioms.html
        #http://effbot.org/tkinterbook/tkinter-file-dialogs.htm
        #http://www.tkdocs.com/tutorial/tree.html
        #http://effbot.org/tkinterbook/listbox.htm

        # Loop
        front.mainloop()

        # https://docs.python.org/3.3/library/tkinter.ttk.html
        # https://github.com/RedFantom/ttkthemes
        # I could use the ttk module but I need to focus on other areas. Backburner.

def main():
    firstRun = SurufelCore()
    firstRun.scannerMainframe()

    #firstSiferRun = SiferCore()
    #

if __name__ == '__main__':
    main()
