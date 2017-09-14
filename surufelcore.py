# https://github.com/Surufel/surufel-scanner

import sys
import pyclamd
import os

import psycopg2

# Python 2
#import Tkinter
#import tkMessageBox

# Python 3
import tkinter
from tkinter import messagebox

class SurufelCore:
    '''A Surufel core that does the magic.'''
    version = 1.002
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

    def surufelReload(self):
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
        front = tkinter.Tk()

        # Title
        front.title("Surufel Scanner Core")

        # Message
        message = "Program Information\n" + "Setting the scanner...\n"
        theFrontMessage = tkinter.Message(front, text=message, width=1000)
        theFrontMessage.pack()

        # Version
        versionButton = tkinter.Button(front, text="Version", command=self.versionCallback)
        versionButton.pack(side='left')

        # Quit Button
        quitButton = tkinter.Button(front, text="Quit", command=quit)
        quitButton.pack(side='left')

        # Loop
        front.mainloop()

def main():
    firstRun = SurufelCore()
    #firstRun.scannerMainframe()
    firstRun.scanCurrentDirectory()
    firstRun.scanCurrentDirectoryNoHidden()

if __name__ == '__main__':
    main()
